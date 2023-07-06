import requests
import argparse
import logging

logger = logging.getLogger(__name__)


class GeoAPI:
    API_KEY = "d81015613923e3e435231f2740d5610b"
    LAT = "-35.836948753554054"
    LON = "-61.870523905384076"

    @staticmethod
    def request_weather_info(url: str) -> dict:
        """Request a Open Weather API para consultar información de datos meteorológicos.

        La función levanta una excepción si el request falla.
        """
        logger.info("Solicitando información(LAT=%s, LON=%s)", GeoAPI.LAT, GeoAPI.LON)
        response = requests.get(url)
        response.raise_for_status()

        return response.json()

    @classmethod
    def is_hot_in_pehuajo(cls, max_temp: int = 28) -> bool:
        """Devuelve True si la temperatura es mayor a `max_temp`. False en otro caso."""
        api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={cls.LAT}&lon={cls.LON}&appid={cls.API_KEY}&units=metric"

        try:
            weather_info = cls.request_weather_info(api_url)
        except requests.exceptions.HTTPError:
            logger.exception("Algo ha salido mal.")
            return False
        else:
            temperature = weather_info["main"]["temp"]
            logger.info("Temperatura en Pehuajó=%d °C.", temperature)
            return temperature > max_temp


def main() -> None:
    # Configurar argumentos y el loggin
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.INFO)

    is_hot = GeoAPI.is_hot_in_pehuajo()
    print(is_hot)


if __name__ == "__main__":
    main()
