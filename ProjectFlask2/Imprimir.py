import win32print
import win32api


def print_pedido(texto, comprovante):
    filename = comprovante + ".txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(texto)
    # win32print.SetDefaultPrinter('L355 Series(Rede)')
    win32print.SetDefaultPrinter('Microsoft Print to PDF')
    win32api.ShellExecute(
        0,
        "print",
        filename,
        '"%s"' % win32print.GetDefaultPrinter(),
        ".",
        0
    )