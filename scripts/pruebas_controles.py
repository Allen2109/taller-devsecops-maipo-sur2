"""Genera defectos ficticios temporales; comprueba detección, sin ejecutarlos."""
import json
import subprocess
import tempfile
from pathlib import Path


def ejecutar(args, esperado):
    p = subprocess.run(args, capture_output=True, text=True, check=False)
    if p.returncode != esperado:
        raise RuntimeError(f"Control {args[0]}: código {p.returncode}, esperado {esperado}: {p.stderr[-1200:]}")
    return p


def main():
    reports = Path("reports")
    reports.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory() as d:
        t = Path(d)
        # Construcción en memoria: el valor didáctico no se deja en main.
        (t / "config.yaml").write_text("password: " + "LAB-" + "CLORO-2026-" + "DEMO\n")
        ejecutar(["gitleaks", "dir", "--redact", "--config", ".gitleaks.toml", "--report-format", "json", "--report-path", str(reports/"negativo-gitleaks.json"), str(t)], 1)
        (t / "parche.py").write_text("import subprocess\nimport requests\ndef leer(host):\n    salida = subprocess.run('modpoll ' + host, shell=True, capture_output=True)\n    requests.post('https://telemetria.invalid', verify=False, data=salida.stdout)\n")
        ejecutar(["semgrep", "scan", "--metrics", "off", "--config", ".semgrep.yml", "--error", "--no-git-ignore", "--json", "--output", str(reports/"negativo-semgrep.json"), str(t)], 1)
        informe = json.loads((reports/"negativo-semgrep.json").read_text())
        if informe.get("errors"): raise RuntimeError("Reglas Semgrep inválidas")
        resultados = informe["results"]
        ids = {x["check_id"].split(".")[-1] for x in resultados}
        if not {"python-shell-true", "python-tls-sin-validar"}.issubset(ids):
            raise RuntimeError("No se detectaron ambos defectos del parche")
        infra = t / "infra"
        infra.mkdir()
        (infra/"panel.yaml").write_text("sistema: panel-operacional-laboratorio\norigenes_permitidos: [0.0.0.0/0]\n")
        ejecutar(["trivy", "config", "--config-check", "policies/", "--check-namespaces", "builtin,user", "--misconfig-scanners", "terraform,yaml", "--rego-error-limit", "0", "--severity", "HIGH,CRITICAL", "--exit-code", "1", "--format", "json", "--output", str(reports/"negativo-trivy.json"), str(infra)], 1)
        datos=json.loads((reports/"negativo-trivy.json").read_text())
        hallazgos=[m for r in datos.get("Results",[]) for m in r.get("Misconfigurations",[]) if m.get("Status")=="FAIL"]
        if not any(m.get("ID")=="LAB-ICS-001" for m in hallazgos): raise RuntimeError("Trivy no detectó la regla de panel operacional")
    (reports/"pruebas-negativas.json").write_text(json.dumps({"gitleaks":"detectado", "semgrep_shell":"detectado", "semgrep_tls":"detectado", "trivy_infra":"detectado", "codigo_inseguro_ejecutado":False}, indent=2))
    print("Defectos detectados sin ejecutar código inseguro")

if __name__ == "__main__": main()
