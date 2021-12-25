# para saber las contraseñas del internet
import subprocess
from pprint import pprint
data = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode("utf-8").split("\n")
                                                    # All User Profile en ingles
profiles = [i.split(":")[1][1:-1] for i in data if "Perfil de todos los usuarios" in i]
for i in profiles:
    results = subprocess.check_output(
        ["netsh", "wlan", "show", "profile", i, "key=clear"]
        ).decode("utf-8", "ignore").split("\n")
                                                    # Key content en sistemas en ingles
    results = [b.split(":")[1][1:-1] for b in results if "Contenido de la clave" in b]
    try:
        print("{:<30}| {:<}".format(i, results[0]))
    except IndexError:
        print("{:<30}| {:<}".format(i, ""))