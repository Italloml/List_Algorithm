def estratFoto(n, torcedores):
    dp = [0] * n #  tabela de programação dinâmica
    dp[0] = torcedores[0]
    dp[1] = max(torcedores[0], torcedores[1])
    for i in range(2, n):  # tabela de programação dinâmica
        dp[i] = max(torcedores[i] + dp[i - 2], dp[i - 1]) # inclui o setor i na foto ou não
    return dp[n - 1]

def main():
    n = int(input()) # Entrada
    torcedores = list(map(int, input().split()))
    somaTorcedores = estratFoto(n, torcedores)
    print(somaTorcedores, "torcedores podem ser fotografados.")

if __name__ == "__main__":
    main()