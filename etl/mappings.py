INDICADORES = [
    "QT_VAGA",
    "QT_ING",
    "QT_MAT",
    "QT_CONC",
    "QT_SIT_TRANCADA",
    "QT_SIT_DESVINCULADO",
    "QT_SIT_TRANSFERIDO",
    "QT_PERDA",
]

DIMENSOES = ["ano", "instituicao", "curso", "area", "area_geral", "modalidade"]

REGIAO_POR_UF = {
    "PR": "sul",
    "SC": "sul",
    "RS": "sul",
    "SP": "sudeste",
    "RJ": "sudeste",
    "MG": "sudeste",
    "ES": "sudeste",
    "BA": "nordeste",
    "SE": "nordeste",
    "AL": "nordeste",
    "PE": "nordeste",
    "PB": "nordeste",
    "RN": "nordeste",
    "CE": "nordeste",
    "PI": "nordeste",
    "MA": "nordeste",
    "GO": "centro-oeste",
    "DF": "centro-oeste",
    "MT": "centro-oeste",
    "MS": "centro-oeste",
    "AM": "norte",
    "RR": "norte",
    "AP": "norte",
    "PA": "norte",
    "TO": "norte",
    "RO": "norte",
    "AC": "norte",
}

MAPPING_2003 = {
    "FORME_DISTANCIA.CSV": {
        "QT_ING": [f"C{i}{j}" for i in range(321, 324) for j in range(1, 3)]
        + [f"C33{faixa:02d}{sexo}" for faixa in range(1, 12) for sexo in range(1, 3)]
        + [f"C33{faixa}{sexo}" for faixa in range(12, 23) for sexo in range(1, 3)],
        "QT_MAT": [f"C{i}{j}" for i in range(341, 343) for j in range(1, 3)],
        "QT_CONC": [f"C{i}{j}" for i in range(351, 353) for j in range(1, 3)],
    },
    "FORME_PRESENCIAL.CSV": {
        "QT_VAGA": [f"C85{grupo:02d}{opt}" for grupo in range(1, 13) for opt in range(1, 3)],
        "QT_ING": [f"C27{faixa:02d}{sexo}" for faixa in range(1, 12) for sexo in range(1, 3)]
        + [f"C27{faixa}{sexo}" for faixa in range(12, 23) for sexo in range(1, 3)],
        "QT_MAT": [f"C28{semestre}{sexo_turno}" for semestre in range(1, 3) for sexo_turno in range(1, 5)],
        "QT_PERDA": [f"C1000{i}" for i in range(11, 19)]
        + [f"C1000{i}" for i in range(21, 29)]
        + [f"C1000{i}" for i in range(31, 39)],
        "QT_CONC": [f"C1010{semestre}{sexo_turno}" for semestre in range(1, 3) for sexo_turno in range(1, 5)],
    },
    "GRADUACAO_DISTANCIA.CSV": {
        "QT_VAGA": [f"C84{grupo:02d}1" for grupo in range(1, 13)],
        "QT_ING": [f"C19{faixa:02d}{sexo}" for faixa in range(1, 12) for sexo in range(1, 3)]
        + [f"C19{faixa}{sexo}" for faixa in range(12, 23) for sexo in range(1, 3)],
        "QT_MAT": [f"C20{semestre}{sexo}" for semestre in range(1, 3) for sexo in range(1, 3)],
        "QT_PERDA": [f"C21{tipo}{item}" for tipo in range(1, 3) for item in range(1, 5)],
        "QT_CONC": [f"C22{semestre}{sexo}" for semestre in range(1, 3) for sexo in range(1, 3)]
        + [f"C23{i}" for i in range(1, 5)],
    },
    "GRADUACAO_PRESENCIAL.CSV": {
        "QT_VAGA": [f"C62{grupo:02d}{opt}" for grupo in range(1, 11) for opt in range(1, 3)]
        + [f"C63{grupo:02d}{opt}" for grupo in range(1, 11) for opt in range(1, 3)]
        + [f"C64{grupo:02d}" for grupo in range(1, 21)]
        + [f"C65{grupo:02d}" for grupo in range(1, 21)]
        + [f"C66{grupo:02d}" for grupo in range(1, 21)],
        "QT_ING": [f"C72{grupo:02d}{opt}" for grupo in range(1, 11) for opt in range(1, 5)]
        + [f"C73{grupo:02d}{opt}" for grupo in range(1, 11) for opt in range(1, 5)]
        + [f"C74{i:02d}" for i in range(1, 41)]
        + [f"C75{i:02d}" for i in range(1, 41)]
        + [f"C76{i:02d}" for i in range(1, 41)]
        + [f"C03{grupo:02d}{opt}" for grupo in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15, 16] for opt in range(1, 5)]
        + [f"C77{i:02d}" for i in list(range(1, 13)) + list(range(17, 45)) + list(range(49, 65))]
        + [f"C09{faixa:02d}{sexo}" for faixa in range(1, 23) for sexo in range(1, 3)],
        "QT_MAT": [f"C78{sem}{opt}" for sem in range(1, 3) for opt in range(1, 5)]
        + [f"C04{sem}{opt}" for sem in [2, 3] for opt in range(1, 5)]
        + [f"C11{i}" for i in range(1, 9)]
        + [f"C79{grupo:02d}{opt}" for grupo in [1, 2, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14] for opt in range(1, 5)]
        + [f"C80{i}" for i in range(1, 9)]
        + [f"C12{sem}{opt}" for sem in range(1, 3) for opt in range(1, 7)]
        + [f"C07{sem}{opt}" for sem in range(1, 3) for opt in range(1, 9)],
        "QT_SIT_TRANCADA": [f"C06{sem}{opt}" for sem in [2, 3] for opt in range(1, 5)],
        "QT_PERDA": [f"C10{motivo}{opt}" for motivo in [1, 2, 3] for opt in range(1, 9)],
        "QT_CONC": [f"C81{sem}{opt}" for sem in range(1, 3) for opt in range(1, 5)]
        + [f"C82{grupo}{opt}" for grupo in [1, 2, 3, 4, 5, 7, 8, 10, 11, 12] for opt in range(1, 5)]
        + [f"C83{i}" for i in range(1, 9)],
    },
    "SECOMPLE_PRESENCIAL.CSV": {
        "QT_ING": [f"C37{faixa:02d}{sexo}" for faixa in range(1, 12) for sexo in range(1, 3)]
        + [f"C37{faixa}{sexo}" for faixa in range(12, 23) for sexo in range(1, 3)],
        "QT_MAT": [f"C38{semestre}{sexo_turno}" for semestre in range(1, 3) for sexo_turno in range(1, 5)],
        "QT_CONC": [f"C39{semestre}{sexo}" for semestre in range(1, 3) for sexo in range(1, 3)],
    },
}
