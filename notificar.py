import sys
from plyer import notification # type: ignore

if len(sys.argv) < 3:
    sys.exit(1)

titulo = sys.argv[1]
mensagem = sys.argv[2]

notification.notify(
    title=titulo,
    message=mensagem,
    timeout=10
)
