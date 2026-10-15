#!/usr/bin/env bash
set -euo pipefail
export PATH="$PWD/.tools:$PATH"
mkdir -p reports
# Gitleaks revisa los archivos productivos y, aparte, el historial de main.
gitleaks dir --redact --config .gitleaks.toml --report-format json --report-path reports/gitleaks.json .
gitleaks git --redact --config .gitleaks.toml --log-opts="main" --report-format json --report-path reports/gitleaks-historial.json .
semgrep scan --metrics off --config .semgrep.yml --error --json --output reports/semgrep.json lector_cloro.py src scripts tests
trivy fs --scanners vuln --severity HIGH,CRITICAL --exit-code 1 --format json --output reports/trivy-dependencias.json requirements.txt
osv-scanner scan source --lockfile requirements.txt --format json --output reports/osv.json
trivy config --config-check policies/ --check-namespaces builtin,user --misconfig-scanners terraform,yaml --rego-error-limit 0 --severity HIGH,CRITICAL --exit-code 1 --format json --output reports/trivy-infra.json infra/
trivy fs --format cyclonedx --output reports/sbom.cdx.json requirements.txt
