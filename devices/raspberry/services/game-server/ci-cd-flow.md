Developer
   |
   | git push main
   v
GitLab CI
   |
   |-- secret scan
   |
   |-- mirror to GitHub
   |
   |-- docker buildx
   |      |
   |      v
   |   ghcr.io/stefi-milo/game:<commit_sha>
   |
   |-- Raspberry deploy runner
          |
          SSH
          |
          v
 Raspberry Pi
          |
          docker pull game:<commit_sha>
          |
          stop old home-arcade
          |
          run new home-arcade
          |
          port 8080:80
