import win32print
import win32api


def print_pedido(texto, comprovante):
    filename = comprovante + ".txt"
    with open(filename, "w", encoding="Utf-8") as f:
        f.write(texto)
    # win32print.SetDefaultPrinter('MP-4200 TH')
    # win32print.SetDefaultPrinter('MP-4000 TH')
    # win32print.SetDefaultPrinter('MP-4000 TH')
    win32print.SetDefaultPrinter('Microsoft Print to PDF')
    win32api.ShellExecute(
        0,
        "print",
        filename,
        '"%s"' % win32print.GetDefaultPrinter(),
        ".",
        0
    )
