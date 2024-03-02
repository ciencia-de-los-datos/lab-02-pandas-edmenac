"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
import pandas as pd
import warnings

warnings.filterwarnings("ignore")

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():
    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40

    """
    num_filas = tbl0.shape[0]

    return num_filas


def pregunta_02():
    """
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?

    Rta/
    4

    """
    num_columnas = tbl0.shape[1]
    
    return num_columnas


def pregunta_03():
    """
    ¿Cuál es la cantidad de registros por cada letra de la columna _c1 del archivo
    `tbl0.tsv`?

    Rta/
    A     8
    B     7
    C     5
    D     6
    E    14
    Name: _c1, dtype: int64

    """
    cantidad_registros = tbl0["_c1"].value_counts().sort_index()

    return cantidad_registros


def pregunta_04():
    """
    Calcule el promedio de _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.

    Rta/
    A    4.625000
    B    5.142857
    C    5.400000
    D    3.833333
    E    4.785714
    Name: _c2, dtype: float64
    """
    promedio = tbl0.groupby("_c1")["_c2"].mean().sort_index()
    
    return promedio


def pregunta_05():
    """
    Calcule el valor máximo de _c2 por cada letra en la columna _c1 del archivo
    `tbl0.tsv`.

    Rta/
    _c1
    A    9
    B    9
    C    9
    D    7
    E    9
    Name: _c2, dtype: int64
    """
    maximo = tbl0.groupby("_c1")["_c2"].max()
    
    return maximo


def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna _c4 de del archivo `tbl1.csv`
    en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
    valores_unicos = tbl1["_c4"].unique()
    valores_unicos = [x.upper() for x in valores_unicos]
    
    return sorted(valores_unicos)


def pregunta_07():
    """
    Calcule la suma de la _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.

    Rta/
    _c1
    A    37
    B    36
    C    27
    D    23
    E    67
    Name: _c2, dtype: int64
    """
    suma = tbl0.groupby("_c1")["_c2"].sum()

    return suma


def pregunta_08():
    """
    Agregue una columna llamada `suma` con la suma de _c0 y _c2 al archivo `tbl0.tsv`.

    Rta/
        _c0 _c1  _c2         _c3  suma
    0     0   E    1  1999-02-28     1
    1     1   A    2  1999-10-28     3
    2     2   B    5  1998-05-02     7
    ...
    37   37   C    9  1997-07-22    46
    38   38   E    1  1999-09-28    39
    39   39   E    5  1998-01-26    44

    """
    tabla_08 = tbl0.copy()
    tabla_08["suma"] = tabla_08["_c0"] + tabla_08["_c2"]

    return tabla_08


def pregunta_09():
    """
    Agregue el año como una columna al archivo `tbl0.tsv`.

    Rta/
        _c0 _c1  _c2         _c3  year
    0     0   E    1  1999-02-28  1999
    1     1   A    2  1999-10-28  1999
    2     2   B    5  1998-05-02  1998
    ...
    37   37   C    9  1997-07-22  1997
    38   38   E    1  1999-09-28  1999
    39   39   E    5  1998-01-26  1998

    """
    tabla_09 = tbl0.copy()
    tabla_09["year"] = tabla_09["_c3"].str[:4]
    
    return tabla_09


def pregunta_10():
    """
    Construya una tabla que contenga _c1 y una lista separada por ':' de los valores de
    la columna _c2 para el archivo `tbl0.tsv`.

    Rta/
                                   _c1
      _c0
    0   A              1:1:2:3:6:7:8:9
    1   B                1:3:4:5:6:8:9
    2   C                    0:5:6:7:9
    3   D                  1:2:3:5:5:7
    4   E  1:1:2:3:3:4:5:5:5:6:7:8:8:9
    """
    tbl0["_c2"] = tbl0["_c2"].astype(str)
    tabla_10 = tbl0.groupby("_c1")["_c2"].apply(lambda x: ":".join(x)).reset_index()
    tabla_10["_c2"] = tabla_10["_c2"].str.split(":").apply(sorted).apply(lambda x: ":".join(x))
    tabla_10.set_index("_c1", inplace=True)

    return tabla_10


def pregunta_11():
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c4 del archivo `tbl1.tsv`.

    Rta/
        _c0      _c4
    0     0    b,f,g
    1     1    a,c,f
    2     2  a,c,e,f
    3     3      a,b
    ...
    37   37  a,c,e,f
    38   38      d,e
    39   39    a,d,f
    """
    tbl1["_c4"] = tbl1["_c4"].astype(str)
    tabla_11 = tbl1.groupby("_c0")["_c4"].apply(lambda x: ",".join(x)).reset_index()
    tabla_11["_c4"] = tabla_11["_c4"].str.split(",").apply(sorted).apply(lambda x: ",".join(x))
    
    return tabla_11


def pregunta_12():
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c5a y _c5b (unidos por ':') de la tabla `tbl2.tsv`.

    Rta/
        _c0                                  _c5
    0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
    1     1              aaa:3,ccc:2,ddd:0,hhh:9
    2     2              ccc:6,ddd:2,ggg:5,jjj:1
    ...
    37   37                    eee:0,fff:2,hhh:6
    38   38                    eee:0,fff:9,iii:2
    39   39                    ggg:3,hhh:8,jjj:5
    """
    tbl2["_c5a"] = tbl2["_c5a"].astype(str)
    tbl2["_c5b"] = tbl2["_c5b"].astype(str)
    tabla_12 = tbl2.groupby("_c0").apply(lambda x: ",".join(x["_c5a"] + ":" + x["_c5b"])).reset_index()
    tabla_12.columns = ["_c0", "_c5"]
    tabla_12["_c5"] = tabla_12["_c5"].str.split(",").apply(sorted).apply(lambda x: ",".join(x))

    return tabla_12


def pregunta_13():
    """
    Si la columna _c0 es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`, compute la
    suma de tbl2._c5b por cada valor en tbl0._c1.

    Rta/
    _c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: _c5b, dtype: int64
    """
    tbl2["_c5b"] = tbl2["_c5b"].astype("int64")
    suma_13 = tbl0.merge(tbl2, on="_c0").groupby("_c1")["_c5b"].sum()

    return suma_13

# def main():
    # print(pregunta_01())
    # print(pregunta_02())
    # print(pregunta_03())
    # print(pregunta_04())
    # print(pregunta_05())
    # print(pregunta_06())
    # print(pregunta_07())
    # print(pregunta_08())
    # print(pregunta_09())
    # print(pregunta_10())
    # print(pregunta_11())
    # print(pregunta_12())
    # print(pregunta_13())

def main():
    pregunta_01()
    pregunta_02()
    pregunta_03()
    pregunta_04()
    pregunta_05()
    pregunta_06()
    pregunta_07()
    pregunta_08()
    pregunta_09()
    pregunta_10()
    pregunta_11()
    pregunta_12()
    pregunta_13()


if __name__ == "__main__":
    main()
