      - name: SAST (Bandit)
        run: bandit -r . -ll

      - name: Dependency scan (pip-audit)
        if: always()
        run: pip-audit || true

      - name: Secret scan (gitleaks)
        if: always()
        uses: gitleaks/gitleaks-action@v2
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
