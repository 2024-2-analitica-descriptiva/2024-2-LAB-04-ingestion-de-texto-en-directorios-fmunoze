# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

import pandas as pd
import glob
import os


def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """

    """
    Genera dos archivos llamados "train_dataset.csv" y "test_dataset.csv"
    con frases y su respectivo sentimiento, a partir de los datos almacenados
    en la carpeta "input" que contiene las subcarpetas "train" y "test".

    Los archivos generados estarán en la carpeta "files/output/".
    """

    # Se crea la carpeta "output" si no existe
    if not os.path.exists("output"):
        os.makedirs("output")

    # Se leen los archivos de la carpeta "train" y se almacenan en un DataFrame
    train_files = glob.glob("files/input/train/*/*.txt")
    train_data = []
    for file in train_files:
        with open(file, "r") as f:
            train_data.append({"phrase": f.read(), "target": file.split("/")[-2]})
    train_df = pd.DataFrame(train_data)

    # Se leen los archivos de la carpeta "test" y se almacenan en un DataFrame
    test_files = glob.glob("files/input/test/*/*.txt")
    test_data = []
    for file in test_files:
        with open(file, "r") as f:
            test_data.append({"phrase": f.read(), "target": file.split("/")[-2]})
    test_df = pd.DataFrame(test_data)

    # Se guardan los DataFrames en archivos CSV
    train_df.to_csv("files/output/train_dataset.csv", index=False)
    test_df.to_csv("files/output/test_dataset.csv", index=False)


pregunta_01()
