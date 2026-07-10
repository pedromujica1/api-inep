# Configurações das Variáveis Legados

## 2003

```python
CONFIGURACOES = {
    "FORME_DISTANCIA.CSV": {
        "QT_ING": [f"C{i}{j}" for i in range(321, 324) for j in range(1, 3)] + \
                  [f"C33{faixa:02d}{sexo}" for faixa in range(1, 12) for sexo in range(1, 3)] + \
                  [f"C33{faixa}{sexo}" for faixa in range(12, 23) for sexo in range(1, 3)],
        "QT_MAT": [f"C{i}{j}" for i in range(341, 343) for j in range(1, 3)],
        "QT_CONC": [f"C{i}{j}" for i in range(351, 353) for j in range(1, 3)]
    },
    "FORME_PRESENCIAL.CSV": {
        "QT_VAGAS": [f"C85{grupo:02d}{opt}" for grupo in range(1, 13) for opt in range(1, 3)],
        "QT_ING": [f"C27{faixa:02d}{sexo}" for faixa in range(1, 12) for sexo in range(1, 3)] + \
                  [f"C27{faixa}{sexo}" for faixa in range(12, 23) for sexo in range(1, 3)],
        "QT_MAT": [f"C28{semestre}{sexo_turno}" for semestre in range(1, 3) for sexo_turno in range(1, 5)],
        "QT_PERDA": [f"C1000{i}" for i in range(11, 19)] + \
                    [f"C1000{i}" for i in range(21, 29)] + \
                    [f"C1000{i}" for i in range(31, 39)],
        "QT_CONC": [f"C1010{semestre}{sexo_turno}" for semestre in range(1, 3) for sexo_turno in range(1, 5)]
    },
    "GRADUACAO_DISTANCIA.CSV": {
        "QT_VAGAS": [f"C84{grupo:02d}1" for grupo in range(1, 13)],
        "QT_ING": [f"C19{faixa:02d}{sexo}" for faixa in range(1, 12) for sexo in range(1, 3)] + \
                  [f"C19{faixa}{sexo}" for faixa in range(12, 23) for sexo in range(1, 3)],
        "QT_MAT": [f"C20{semestre}{sexo}" for semestre in range(1, 3) for sexo in range(1, 3)],
        "QT_PERDA": [f"C21{tipo}{item}" for tipo in range(1, 3) for item in range(1, 5)],
        "QT_CONC": [f"C22{semestre}{sexo}" for semestre in range(1, 3) for sexo in range(1, 3)] + \
                   [f"C23{i}" for i in range(1, 5)]
    },
    "GRADUACAO_PRESENCIAL.CSV": {
        "QT_VAGAS": [f"C62{grupo:02d}{opt}" for grupo in range(1, 11) for opt in range(1, 3)] + \
                    [f"C63{grupo:02d}{opt}" for grupo in range(1, 11) for opt in range(1, 3)] + \
                    [f"C64{grupo:02d}" for grupo in range(1, 21)] + \
                    [f"C65{grupo:02d}" for grupo in range(1, 21)] + \
                    [f"C66{grupo:02d}" for grupo in range(1, 21)],
        "QT_ING": [f"C72{grupo:02d}{opt}" for grupo in range(1, 11) for opt in range(1, 5)] + \
                  [f"C73{grupo:02d}{opt}" for grupo in range(1, 11) for opt in range(1, 5)] + \
                  [f"C74{i:02d}" for i in range(1, 41)] + \
                  [f"C75{i:02d}" for i in range(1, 41)] + \
                  [f"C76{i:02d}" for i in range(1, 41)] + \
                  [f"C03{grupo:02d}{opt}" for grupo in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15, 16] for opt in range(1, 5)] + \
                  [f"C77{i:02d}" for i in list(range(1, 13)) + list(range(17, 45)) + list(range(49, 65))] + \
                  [f"C09{faixa:02d}{sexo}" for faixa in range(1, 23) for sexo in range(1, 3)],
        "QT_MAT": [f"C78{sem}{opt}" for sem in range(1, 3) for opt in range(1, 5)] + \
                  [f"C04{sem}{opt}" for sem in [2, 3] for opt in range(1, 5)] + \
                  [f"C11{i}" for i in range(1, 9)] + \
                  [f"C79{grupo:02d}{opt}" for grupo in [1, 2, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14] for opt in range(1, 5)] + \
                  [f"C80{i}" for i in range(1, 9)] + \
                  [f"C12{sem}{opt}" for sem in range(1, 3) for opt in range(1, 7)] + \
                  [f"C07{sem}{opt}" for sem in range(1, 3) for opt in range(1, 9)],
        "QT_SIT_TRANCADA": [f"C06{sem}{opt}" for sem in [2, 3] for opt in range(1, 5)],
        "QT_PERDA": [f"C10{motivo}{opt}" for motivo in [1, 2, 3] for opt in range(1, 9)],
        "QT_CONC": [f"C81{sem}{opt}" for sem in range(1, 3) for opt in range(1, 5)] + \
                   [f"C82{grupo}{opt}" for grupo in [1, 2, 3, 4, 5, 7, 8, 10, 11, 12] for opt in range(1, 5)] + \
                   [f"C83{i}" for i in range(1, 9)]
    },
    "SECOMPLE_PRESENCIAL.CSV": {
        "QT_ING": [f"C37{faixa:02d}{sexo}" for faixa in range(1, 12) for sexo in range(1, 3)] + \
                  [f"C37{faixa}{sexo}" for faixa in range(12, 23) for sexo in range(1, 3)],
        "QT_MAT": [f"C38{semestre}{sexo_turno}" for semestre in range(1, 3) for sexo_turno in range(1, 5)],
        "QT_CONC": [f"C39{semestre}{sexo}" for semestre in range(1, 3) for sexo in range(1, 3)]
    }
}

```

## 2004

```python
CONFIGURACOES = {
    "FORME_DISTANCIA.CSV": {
        "QT_ING": ["C109011", "C109041"] + \
                  [f"C33{faixa:02d}{sexo}" for faixa in range(1, 12) for sexo in range(1, 3)] + \
                  [f"C33{faixa}{sexo}" for faixa in range(12, 23) for sexo in range(1, 3)],
        "QT_MAT": [f"C{i}{j}" for i in range(341, 343) for j in range(1, 3)],
        "QT_SIT_TRANCADA": [f"C1190{grupo}{opt}" for grupo in range(1, 9) for opt in range(1, 3)],
        "QT_CONC": [f"C{i}{j}" for i in range(351, 353) for j in range(1, 3)]
    },
    "FORME_PRESENCIAL.CSV": {
        "QT_VAGAS": ["C85011", "C85012", "C85021", "C85022", "C85033", "C85034", "C85043", "C85044",
                     "C85053", "C85054", "C85071", "C85072", "C85081", "C85082", "C85093", "C85094",
                     "C85103", "C85104", "C85113", "C85114"],
        "QT_ING": [f"C27{faixa:02d}{sexo}" for faixa in range(1, 12) for sexo in range(1, 3)] + \
                  [f"C27{faixa}{sexo}" for faixa in range(12, 23) for sexo in range(1, 3)],
        "QT_MAT": [f"C28{semestre}{sexo_turno}" for semestre in range(1, 3) for sexo_turno in range(1, 5)],
        "QT_PERDA": [f"C1000{i}" for i in range(11, 19)] + \
                    [f"C1000{i}" for i in range(21, 29)] + \
                    [f"C1000{i}" for i in range(31, 39)] + \
                    [f"C1000{i}" for i in range(41, 49)],
        "QT_CONC": [f"C1010{semestre}{sexo_turno}" for semestre in range(1, 3) for sexo_turno in range(1, 5)]
    },
    "GRADUACAO_DISTANCIA.CSV": {
        "QT_VAGAS": ["C84011", "C84021", "C84031", "C84041", "C84051", 
                     "C84071", "C84081", "C84091", "C84101", "C84111"],
        "QT_ING": [f"C19{faixa:02d}{sexo}" for faixa in range(1, 12) for sexo in range(1, 3)] + \
                  [f"C19{faixa}{sexo}" for faixa in range(12, 23) for sexo in range(1, 3)],
        "QT_MAT": [f"C20{semestre}{sexo}" for semestre in range(1, 3) for sexo in range(1, 3)],
        "QT_PERDA": [f"C21{tipo}{item}" for tipo in range(1, 5) for item in range(1, 5)],
        "QT_CONC": [f"C22{semestre}{sexo}" for semestre in range(1, 3) for sexo in range(1, 3)] + \
                   [f"C23{i}" for i in range(1, 5)]
    },
    "GRADUACAO_PRESENCIAL.CSV": {
        "QT_VAGAS": [f"C62{grupo:02d}{opt}" for grupo in range(1, 11) for opt in range(1, 3)] + \
                    [f"C63{grupo:02d}{opt}" for grupo in range(1, 11) for opt in range(1, 3)] + \
                    [f"C64{grupo:02d}" for grupo in range(1, 21)] + \
                    [f"C65{grupo:02d}" for grupo in range(1, 21)] + \
                    [f"C66{grupo:02d}" for grupo in range(1, 21)],
        "QT_ING": [f"C72{grupo:02d}{opt}" for grupo in range(1, 11) for opt in range(1, 5)] + \
                  [f"C73{grupo:02d}{opt}" for grupo in range(1, 11) for opt in range(1, 5)] + \
                  [f"C74{i:02d}" for i in range(1, 41)] + \
                  [f"C75{i:02d}" for i in range(1, 41)] + \
                  [f"C76{i:02d}" for i in range(1, 41)] + \
                  [f"C03{grupo:02d}{opt}" for grupo in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15, 16] for opt in range(1, 5)] + \
                  [f"C77{i:02d}" for i in list(range(1, 13)) + list(range(17, 45)) + list(range(49, 65))] + \
                  [f"C09{faixa:02d}{sexo}" for faixa in range(1, 23) for sexo in range(1, 3)],
        "QT_MAT": [f"C78{sem}{opt}" for sem in range(1, 3) for opt in range(1, 5)] + \
                  [f"C04{sem}{opt}" for sem in [2, 3] for opt in range(1, 5)] + \
                  [f"C11{i}" for i in range(1, 9)] + \
                  [f"C79{grupo:02d}{opt}" for grupo in [1, 2, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14] for opt in range(1, 5)] + \
                  [f"C80{i}" for i in range(1, 9)] + \
                  [f"C12{sem}{opt}" for sem in range(1, 3) for opt in range(1, 7)] + \
                  [f"C07{sem}{opt}" for sem in range(1, 3) for opt in range(1, 9)],
        "QT_SIT_TRANCADA": [f"C06{sem}{opt}" for sem in [2, 3] for opt in range(1, 5)],
        "QT_PERDA": [f"C10{motivo}{opt}" for motivo in [1, 2, 3] for opt in range(1, 9)],
        "QT_CONC": [f"C81{sem}{opt}" for sem in range(1, 3) for opt in range(1, 5)] + \
                   [f"C82{grupo}{opt}" for grupo in [1, 2, 3, 4, 5, 7, 8, 10, 11, 12] for opt in range(1, 5)] + \
                   [f"C83{i}" for i in range(1, 9)]
    },
    "SECOMPLE_PRESENCIAL.CSV": {
        "QT_VAGAS": ["C112101", "C112102", "C112301", "C112302"],
        "QT_ING": [f"C37{faixa:02d}{sexo}" for faixa in range(1, 12) for sexo in range(1, 3)] + \
                  [f"C37{faixa}{sexo}" for faixa in range(12, 23) for sexo in range(1, 3)],
        "QT_MAT": [f"C38{semestre}{sexo_turno}" for semestre in range(1, 3) for sexo_turno in range(1, 5)],
        "QT_SIT_TRANCADA": [f"C1130{grupo}{opt}" for grupo in range(1, 9) for opt in range(1, 5)],
        "QT_CONC": [f"C39{semestre}{sexo}" for semestre in range(1, 3) for sexo in range(1, 3)]
    }
}

```

## 2005

```python
CONFIGURACOES = {
    "FORME_DISTANCIA.CSV": {
        "QT_VAGAS": ["C109011", "C109041"] + \
                  [f"C33{faixa:02d}{sexo}" for faixa in range(1, 12) for sexo in range(1, 3)] + \
                  [f"C33{faixa}{sexo}" for faixa in range(12, 23) for sexo in range(1, 3)],
        "QT_MAT": [f"C34{semestre}{sexo}" for semestre in range(1, 3) for sexo in range(1, 3)],
        "QT_SIT_TRANCADA": [f"C1190{grupo}{opt}" for grupo in range(1, 9) for opt in range(1, 3)],
        "QT_CONC": [f"C35{semestre}{sexo}" for semestre in range(1, 3) for sexo in range(1, 3)]
    },
    "FORME_PRESENCIAL.CSV": {
        "QT_VAGAS": ["C85011", "C85012", "C85021", "C85022", "C85031", "C85032", "C85041", "C85042",
                     "C85051", "C85052", "C85071", "C85072", "C85081", "C85082", "C85091", "C85092",
                     "C85101", "C85102", "C85111", "C85112"],
        "QT_ING": [f"C27{faixa:02d}{sexo}" for faixa in range(1, 12) for sexo in range(1, 3)] + \
                  [f"C27{faixa}{sexo}" for faixa in range(12, 23) for sexo in range(1, 3)],
        "QT_MAT": [f"C28{semestre}{sexo_turno}" for semestre in range(1, 3) for sexo_turno in range(1, 5)],
        "QT_PERDA": [f"C1000{i}" for i in range(11, 19)] + \
                    [f"C1000{i}" for i in range(21, 29)] + \
                    [f"C1000{i}" for i in range(31, 39)] + \
                    [f"C1000{i}" for i in range(41, 49)],
        "QT_CONC": [f"C1010{semestre}{sexo_turno}" for semestre in range(1, 3) for sexo_turno in range(1, 5)]
    },
    "GRADUACAO_DISTANCIA.CSV": {
        "QT_VAGAS": ["C84011", "C84021", "C84031", "C84041", "C84051", 
                     "C84071", "C84081", "C84091", "C84101", "C84111"],
        "QT_ING": [f"C19{faixa:02d}{sexo}" for faixa in range(1, 12) for sexo in range(1, 3)] + \
                  [f"C19{faixa}{sexo}" for faixa in range(12, 23) for sexo in range(1, 3)],
        "QT_MAT": [f"C20{semestre}{sexo}" for semestre in range(1, 3) for sexo in range(1, 3)],
        "QT_PERDA": [f"C21{tipo}{item}" for tipo in range(1, 5) for item in range(1, 5)],
        "QT_CONC": [f"C22{semestre}{sexo}" for semestre in range(1, 3) for sexo in range(1, 3)] + \
                   [f"C23{i}" for i in range(1, 5)]
    },
    "GRADUACAO_PRESENCIAL.CSV": {
        "QT_VAGAS": [f"C62{grupo:02d}{opt}" for grupo in range(1, 11) for opt in range(1, 3)] + \
                    [f"C63{grupo:02d}{opt}" for grupo in range(1, 11) for opt in range(1, 3)] + \
                    [f"C64{grupo:02d}" for grupo in range(1, 21)] + \
                    [f"C65{grupo:02d}" for grupo in range(1, 21)] + \
                    [f"C66{grupo:02d}" for grupo in range(1, 21)],
        "QT_ING": [f"C72{grupo:02d}{opt}" for grupo in range(1, 11) for opt in range(1, 5)] + \
                  [f"C73{grupo:02d}{opt}" for grupo in range(1, 11) for opt in range(1, 5)] + \
                  [f"C74{i:02d}" for i in range(1, 41)] + \
                  [f"C75{i:02d}" for i in range(1, 41)] + \
                  [f"C76{i:02d}" for i in range(1, 41)] + \
                  [f"C03{grupo:02d}{opt}" for grupo in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15, 16] for opt in range(1, 5)] + \
                  [f"C77{i:02d}" for i in list(range(1, 13)) + list(range(17, 45)) + list(range(49, 65))] + \
                  [f"C09{faixa:02d}{sexo}" for faixa in range(1, 23) for sexo in range(1, 3)],
        "QT_MAT": [f"C78{sem}{opt}" for sem in range(1, 3) for opt in range(1, 5)] + \
                  [f"C04{sem}{opt}" for sem in [2, 3] for opt in range(1, 5)] + \
                  [f"C11{i}" for i in range(1, 9)] + \
                  [f"C79{grupo:02d}{opt}" for grupo in [1, 2, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14] for opt in range(1, 5)] + \
                  [f"C80{i}" for i in range(1, 9)] + \
                  [f"C12{sem}{opt}" for sem in range(1, 3) for opt in range(1, 7)] + \
                  [f"C07{sem}{opt}" for sem in range(1, 3) for opt in range(1, 9)],
        "QT_SIT_TRANCADA": [f"C06{sem}{opt}" for sem in [2, 3] for opt in range(1, 5)],
        "QT_PERDA": [f"C10{motivo}{opt}" for motivo in [1, 2, 3] for opt in range(1, 9)],
        "QT_CONC": [f"C81{sem}{opt}" for sem in range(1, 3) for opt in range(1, 5)] + \
                   [f"C82{grupo}{opt}" for grupo in [1, 2, 3, 4, 5, 7, 8, 10, 11, 12] for opt in range(1, 5)] + \
                   [f"C83{i}" for i in range(1, 9)]
    },
    "SECOMPLE_PRESENCIAL.CSV": {
        "QT_VAGAS": [# Q59.A3 - Vagas/Inscritos/Ingressantes (Nova Questão 2004)
            "C112101", "C112102", "C112201", "C112202","C112301","C112302","C112401","C112402"],
        "QT_ING": [f"C37{faixa:02d}{sexo}" for faixa in range(1, 12) for sexo in range(1, 3)] + \
                  [f"C37{faixa}{sexo}" for faixa in range(12, 23) for sexo in range(1, 3)],
        "QT_MAT": [f"C38{semestre}{sexo_turno}" for semestre in range(1, 3) for sexo_turno in range(1, 5)],
        "QT_SIT_TRANCADA": [f"C1130{grupo}{opt}" for grupo in range(1, 9) for opt in range(1, 5)],
        "QT_CONC": [f"C39{semestre}{sexo}" for semestre in range(1, 3) for sexo in range(1, 5)]
    }
}

```


## 2006

```python
CONFIGURACOES = {
    "FORME_DISTANCIA.CSV": {
        "QT_VAGAS": ["C109011", "C109041"] + \
                  [f"C33{faixa:02d}{sexo}" for faixa in range(1, 12) for sexo in range(1, 3)] + \
                  [f"C33{faixa}{sexo}" for faixa in range(12, 23) for sexo in range(1, 3)],
        "QT_MAT": [f"C34{semestre}{sexo}" for semestre in range(1, 3) for sexo in range(1, 3)],
        "QT_SIT_TRANCADA": [f"C1190{grupo}{opt}" for grupo in range(1, 9) for opt in range(1, 3)],
        "QT_CONC": [f"C35{semestre}{sexo}" for semestre in range(1, 3) for sexo in range(1, 3)]
    },
    "FORME_PRESENCIAL.CSV": {
        "QT_VAGAS": ["C85011", "C85012", "C85021", "C85022", "C85031", "C85032", "C85041", "C85042",
                     "C85051", "C85052", "C85071", "C85072", "C85081", "C85082", "C85091", "C85092",
                     "C85101", "C85102", "C85111", "C85112"],
        "QT_ING": [f"C27{faixa:02d}{sexo}" for faixa in range(1, 12) for sexo in range(1, 3)] + \
                  [f"C27{faixa}{sexo}" for faixa in range(12, 23) for sexo in range(1, 3)],
        "QT_MAT": [f"C28{semestre}{sexo_turno}" for semestre in range(1, 3) for sexo_turno in range(1, 5)],
        "QT_PERDA": [f"C1000{i}" for i in range(11, 19)] + \
                    [f"C1000{i}" for i in range(21, 29)] + \
                    [f"C1000{i}" for i in range(31, 39)] + \
                    [f"C1000{i}" for i in range(41, 49)],
        "QT_CONC": [f"C1010{semestre}{sexo_turno}" for semestre in range(1, 3) for sexo_turno in range(1, 5)]
    },
    "GRADUACAO_DISTANCIA.CSV": {
        "QT_VAGAS": ["C84011", "C84021", "C84031", "C84041", "C84051", 
                     "C84071", "C84081", "C84091", "C84101", "C84111"],
        "QT_ING": [f"C19{faixa:02d}{sexo}" for faixa in range(1, 12) for sexo in range(1, 3)] + \
                  [f"C19{faixa}{sexo}" for faixa in range(12, 23) for sexo in range(1, 3)],
        "QT_MAT": [f"C20{semestre}{sexo}" for semestre in range(1, 3) for sexo in range(1, 3)],
        "QT_PERDA": [f"C21{tipo}{item}" for tipo in range(1, 5) for item in range(1, 5)],
        "QT_CONC": [f"C22{semestre}{sexo}" for semestre in range(1, 3) for sexo in range(1, 3)] + \
                   [f"C23{i}" for i in range(1, 5)]
    },
    "GRADUACAO_PRESENCIAL.CSV": {
        "QT_VAGAS": [f"C62{grupo:02d}{opt}" for grupo in range(1, 11) for opt in range(1, 3)] + \
                    [f"C63{grupo:02d}{opt}" for grupo in range(1, 11) for opt in range(1, 3)] + \
                    [f"C64{grupo:02d}" for grupo in range(1, 21)] + \
                    [f"C65{grupo:02d}" for grupo in range(1, 21)] + \
                    [f"C66{grupo:02d}" for grupo in range(1, 21)],
        "QT_ING": [f"C72{grupo:02d}{opt}" for grupo in range(1, 11) for opt in range(1, 5)] + \
                  [f"C73{grupo:02d}{opt}" for grupo in range(1, 11) for opt in range(1, 5)] + \
                  [f"C74{i:02d}" for i in range(1, 41)] + \
                  [f"C75{i:02d}" for i in range(1, 41)] + \
                  [f"C76{i:02d}" for i in range(1, 41)] + \
                  [f"C03{grupo:02d}{opt}" for grupo in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15, 16] for opt in range(1, 5)] + \
                  [f"C77{i:02d}" for i in list(range(1, 13)) + list(range(17, 45)) + list(range(49, 65))] + \
                  [f"C09{faixa:02d}{sexo}" for faixa in range(1, 23) for sexo in range(1, 3)],
        "QT_MAT": [f"C78{sem}{opt}" for sem in range(1, 3) for opt in range(1, 5)] + \
                  [f"C04{sem}{opt}" for sem in [2, 3] for opt in range(1, 5)] + \
                  [f"C11{i}" for i in range(1, 9)] + \
                  [f"C79{grupo:02d}{opt}" for grupo in [1, 2, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14] for opt in range(1, 5)] + \
                  [f"C80{i}" for i in range(1, 9)] + \
                  [f"C12{sem}{opt}" for sem in range(1, 3) for opt in range(1, 7)] + \
                  [f"C07{sem}{opt}" for sem in range(1, 3) for opt in range(1, 9)],
        "QT_SIT_TRANCADA": [f"C06{sem}{opt}" for sem in [2, 3] for opt in range(1, 5)],
        "QT_PERDA": [f"C10{motivo}{opt}" for motivo in [1, 2, 3] for opt in range(1, 9)],
        "QT_CONC": [f"C81{sem}{opt}" for sem in range(1, 3) for opt in range(1, 5)] + \
                   [f"C82{grupo}{opt}" for grupo in [1, 2, 3, 4, 5, 7, 8, 10, 11, 12] for opt in range(1, 5)] + \
                   [f"C83{i}" for i in range(1, 9)]
    },
    "SECOMPLE_PRESENCIAL.CSV": {
        "QT_VAGAS": [# Q59.A3 - Vagas/Inscritos/Ingressantes (Nova Questão 2004)
            "C112101", "C112102", "C112201", "C112202","C112301","C112302","C112401","C112402"],
        "QT_ING": [f"C37{faixa:02d}{sexo}" for faixa in range(1, 12) for sexo in range(1, 3)] + \
                  [f"C37{faixa}{sexo}" for faixa in range(12, 23) for sexo in range(1, 3)],
        "QT_MAT": [f"C38{semestre}{sexo_turno}" for semestre in range(1, 3) for sexo_turno in range(1, 5)],
        "QT_SIT_TRANCADA": [f"C1130{grupo}{opt}" for grupo in range(1, 9) for opt in range(1, 5)],
        "QT_CONC": [f"C39{semestre}{sexo}" for semestre in range(1, 3) for sexo in range(1, 5)]
    },
    "SECOMPLE_DISTANCIA.CSV": {
        "QT_VAGAS": ["C117011", "C117021", "C117041", "C117051"],
        "QT_ING": [f"C37{faixa:02d}{sexo}" for faixa in range(1, 12) for sexo in range(1, 3)] + \
                  [f"C37{faixa}{sexo}" for faixa in range(12, 23) for sexo in range(1, 3)],
        "QT_MAT": [f"C38{semestre}{sexo_turno}" for semestre in range(1, 3) for sexo_turno in range(1, 5)],
        "QT_SIT_TRANCADA": [f"C1130{grupo}{opt}" for grupo in range(1, 9) for opt in range(1, 5)],
        "QT_CONC": [f"C39{semestre}{sexo_turno}" for semestre in range(1, 3) for sexo_turno in range(1, 5)]
    }
}

```

## 2007

```python
CONFIGURACOES = {
    "FORME_DISTANCIA.CSV": {
        "QT_VAGAS": ["C109011", "C109041"] + \
                  [f"C33{faixa:02d}{sexo}" for faixa in range(1, 12) for sexo in range(1, 3)] + \
                  [f"C33{faixa}{sexo}" for faixa in range(12, 23) for sexo in range(1, 3)],
        "QT_MAT": [f"C34{semestre}{sexo}" for semestre in range(1, 3) for sexo in range(1, 3)],
        "QT_SIT_TRANCADA": [f"C1190{grupo}{opt}" for grupo in range(1, 9) for opt in range(1, 3)],
        "QT_CONC": [f"C35{semestre}{sexo}" for semestre in range(1, 3) for sexo in range(1, 3)]
    },
    "FORME_PRESENCIAL.CSV": {
        "QT_VAGAS": ["C85011", "C85012", "C85021", "C85022", "C85031", "C85032", "C85041", "C85042",
                     "C85051", "C85052", "C85071", "C85072", "C85081", "C85082", "C85091", "C85092",
                     "C85101", "C85102", "C85111", "C85112"],
        "QT_ING": [f"C27{faixa:02d}{sexo}" for faixa in range(1, 12) for sexo in range(1, 3)] + \
                  [f"C27{faixa}{sexo}" for faixa in range(12, 23) for sexo in range(1, 3)],
        "QT_MAT": [f"C28{semestre}{sexo_turno}" for semestre in range(1, 3) for sexo_turno in range(1, 5)],
        "QT_PERDA": [f"C1000{i}" for i in range(11, 19)] + \
                    [f"C1000{i}" for i in range(21, 29)] + \
                    [f"C1000{i}" for i in range(31, 39)] + \
                    [f"C1000{i}" for i in range(41, 49)],
        "QT_CONC": [f"C1010{semestre}{sexo_turno}" for semestre in range(1, 3) for sexo_turno in range(1, 5)]
    },
    "GRADUACAO_DISTANCIA.CSV": {
        "QT_VAGAS": ["C84011", "C84021", "C84031", "C84041", "C84051", 
                     "C84071", "C84081", "C84091", "C84101", "C84111"],
        "QT_ING": [f"C19{faixa:02d}{sexo}" for faixa in range(1, 12) for sexo in range(1, 3)] + \
                  [f"C19{faixa}{sexo}" for faixa in range(12, 23) for sexo in range(1, 3)],
        "QT_MAT": [f"C20{semestre}{sexo}" for semestre in range(1, 3) for sexo in range(1, 3)],
        "QT_PERDA": [f"C21{tipo}{item}" for tipo in range(1, 5) for item in range(1, 5)],
        "QT_CONC": [f"C22{semestre}{sexo}" for semestre in range(1, 3) for sexo in range(1, 3)] + \
                   [f"C23{i}" for i in range(1, 5)]
    },
    "GRADUACAO_PRESENCIAL.CSV": {
        "QT_VAGAS": [f"C62{grupo:02d}{opt}" for grupo in range(1, 11) for opt in range(1, 3)] + \
                    [f"C63{grupo:02d}{opt}" for grupo in range(1, 11) for opt in range(1, 3)] + \
                    [f"C64{grupo:02d}" for grupo in range(1, 21)] + \
                    [f"C65{grupo:02d}" for grupo in range(1, 21)] + \
                    [f"C66{grupo:02d}" for grupo in range(1, 21)],
        "QT_ING": [f"C72{grupo:02d}{opt}" for grupo in range(1, 11) for opt in range(1, 5)] + \
                  [f"C73{grupo:02d}{opt}" for grupo in range(1, 11) for opt in range(1, 5)] + \
                  [f"C74{i:02d}" for i in range(1, 41)] + \
                  [f"C75{i:02d}" for i in range(1, 41)] + \
                  [f"C76{i:02d}" for i in range(1, 41)] + \
                  [f"C03{grupo:02d}{opt}" for grupo in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15, 16] for opt in range(1, 5)] + \
                  [f"C77{i:02d}" for i in list(range(1, 13)) + list(range(17, 45)) + list(range(49, 65))] + \
                  [f"C09{faixa:02d}{sexo}" for faixa in range(1, 23) for sexo in range(1, 3)],
        "QT_MAT": [f"C78{sem}{opt}" for sem in range(1, 3) for opt in range(1, 5)] + \
                  [f"C04{sem}{opt}" for sem in [2, 3] for opt in range(1, 5)] + \
                  [f"C11{i}" for i in range(1, 9)] + \
                  [f"C79{grupo:02d}{opt}" for grupo in [1, 2, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14] for opt in range(1, 5)] + \
                  [f"C80{i}" for i in range(1, 9)] + \
                  [f"C12{sem}{opt}" for sem in range(1, 3) for opt in range(1, 7)] + \
                  [f"C07{sem}{opt}" for sem in range(1, 3) for opt in range(1, 9)],
        "QT_SIT_TRANCADA": [f"C06{sem}{opt}" for sem in [2, 3] for opt in range(1, 5)],
        "QT_PERDA": [f"C10{motivo}{opt}" for motivo in [1, 2, 3] for opt in range(1, 9)],
        "QT_CONC": [f"C81{sem}{opt}" for sem in range(1, 3) for opt in range(1, 5)] + \
                   [f"C82{grupo}{opt}" for grupo in [1, 2, 3, 4, 5, 7, 8, 10, 11, 12] for opt in range(1, 5)] + \
                   [f"C83{i}" for i in range(1, 9)]
    },
    "SECOMPLE_PRESENCIAL.CSV": {
        "QT_VAGAS": [# Q59.A3 - Vagas/Inscritos/Ingressantes (Nova Questão 2004)
            "C112101", "C112102", "C112201", "C112202","C112301","C112302","C112401","C112402"],
        "QT_ING": [f"C37{faixa:02d}{sexo}" for faixa in range(1, 12) for sexo in range(1, 3)] + \
                  [f"C37{faixa}{sexo}" for faixa in range(12, 23) for sexo in range(1, 3)],
        "QT_MAT": [f"C38{semestre}{sexo_turno}" for semestre in range(1, 3) for sexo_turno in range(1, 5)],
        "QT_SIT_TRANCADA": [f"C1130{grupo}{opt}" for grupo in range(1, 9) for opt in range(1, 5)],
        "QT_CONC": [f"C39{semestre}{sexo}" for semestre in range(1, 3) for sexo in range(1, 5)]
    },
    "SECOMPLE_DISTANCIA.CSV": {
        "QT_VAGAS": ["C117011", "C117021", "C117041", "C117051"],
        "QT_ING": [f"C37{faixa:02d}{sexo}" for faixa in range(1, 12) for sexo in range(1, 3)] + \
                  [f"C37{faixa}{sexo}" for faixa in range(12, 23) for sexo in range(1, 3)],
        "QT_MAT": [f"C38{semestre}{sexo_turno}" for semestre in range(1, 3) for sexo_turno in range(1, 5)],
        "QT_SIT_TRANCADA": [f"C1130{grupo}{opt}" for grupo in range(1, 9) for opt in range(1, 5)],
        "QT_CONC": [f"C39{semestre}{sexo_turno}" for semestre in range(1, 3) for sexo_turno in range(1, 5)]
    }
}

```


## 2008

```python
CONFIGURACOES = {
    "FORME_DISTANCIA.CSV": {
        "QT_VAGAS": ["C109011", "C109041"] + \
                  [f"C33{faixa:02d}{sexo}" for faixa in range(1, 12) for sexo in range(1, 3)] + \
                  [f"C33{faixa}{sexo}" for faixa in range(12, 23) for sexo in range(1, 3)],
        "QT_MAT": [f"C34{semestre}{sexo}" for semestre in range(1, 3) for sexo in range(1, 3)],
        "QT_SIT_TRANCADA": [f"C1190{grupo}{opt}" for grupo in range(1, 9) for opt in range(1, 3)],
        "QT_CONC": [f"C35{semestre}{sexo}" for semestre in range(1, 3) for sexo in range(1, 3)]
    },
    "FORME_PRESENCIAL.CSV": {
        "QT_VAGAS": ["C85011", "C85012", "C85021", "C85022", "C85031", "C85032", "C85041", "C85042",
                     "C85051", "C85052", "C85071", "C85072", "C85081", "C85082", "C85091", "C85092",
                     "C85101", "C85102", "C85111", "C85112"],
        "QT_ING": [f"C27{faixa:02d}{sexo}" for faixa in range(1, 12) for sexo in range(1, 3)] + \
                  [f"C27{faixa}{sexo}" for faixa in range(12, 23) for sexo in range(1, 3)],
        "QT_MAT": [f"C28{semestre}{sexo_turno}" for semestre in range(1, 3) for sexo_turno in range(1, 5)],
        "QT_PERDA": [f"C1000{i}" for i in range(11, 19)] + \
                    [f"C1000{i}" for i in range(21, 29)] + \
                    [f"C1000{i}" for i in range(31, 39)] + \
                    [f"C1000{i}" for i in range(41, 49)],
        "QT_CONC": [f"C1010{semestre}{sexo_turno}" for semestre in range(1, 3) for sexo_turno in range(1, 5)]
    },
    "GRADUACAO_DISTANCIA.CSV": {
        "QT_VAGAS": ["C84011", "C84021", "C84031", "C84041", "C84051", 
                     "C84071", "C84081", "C84091", "C84101", "C84111"],
        "QT_ING": [f"C19{faixa:02d}{sexo}" for faixa in range(1, 12) for sexo in range(1, 3)] + \
                  [f"C19{faixa}{sexo}" for faixa in range(12, 23) for sexo in range(1, 3)],
        "QT_MAT": [f"C20{semestre}{sexo}" for semestre in range(1, 3) for sexo in range(1, 3)],
        "QT_PERDA": [f"C21{tipo}{item}" for tipo in range(1, 5) for item in range(1, 5)],
        "QT_CONC": [f"C22{semestre}{sexo}" for semestre in range(1, 3) for sexo in range(1, 3)] + \
                   [f"C23{i}" for i in range(1, 5)]
    },
    "GRADUACAO_PRESENCIAL.CSV": {
        "QT_VAGAS": [f"C62{grupo:02d}{opt}" for grupo in range(1, 11) for opt in range(1, 3)] + \
                    [f"C63{grupo:02d}{opt}" for grupo in range(1, 11) for opt in range(1, 3)] + \
                    [f"C64{grupo:02d}" for grupo in range(1, 21)] + \
                    [f"C65{grupo:02d}" for grupo in range(1, 21)] + \
                    [f"C66{grupo:02d}" for grupo in range(1, 21)],
        "QT_ING": [f"C72{grupo:02d}{opt}" for grupo in range(1, 11) for opt in range(1, 5)] + \
                  [f"C73{grupo:02d}{opt}" for grupo in range(1, 11) for opt in range(1, 5)] + \
                  [f"C74{i:02d}" for i in range(1, 41)] + \
                  [f"C75{i:02d}" for i in range(1, 41)] + \
                  [f"C76{i:02d}" for i in range(1, 41)] + \
                  [f"C03{grupo:02d}{opt}" for grupo in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15, 16] for opt in range(1, 5)] + \
                  [f"C77{i:02d}" for i in list(range(1, 13)) + list(range(17, 45)) + list(range(49, 65))] + \
                  [f"C09{faixa:02d}{sexo}" for faixa in range(1, 23) for sexo in range(1, 3)],
        "QT_MAT": [f"C78{sem}{opt}" for sem in range(1, 3) for opt in range(1, 5)] + \
                  [f"C04{sem}{opt}" for sem in [2, 3] for opt in range(1, 5)] + \
                  [f"C11{i}" for i in range(1, 9)] + \
                  [f"C79{grupo:02d}{opt}" for grupo in [1, 2, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14] for opt in range(1, 5)] + \
                  [f"C80{i}" for i in range(1, 9)] + \
                  [f"C12{sem}{opt}" for sem in range(1, 3) for opt in range(1, 7)] + \
                  [f"C07{sem}{opt}" for sem in range(1, 3) for opt in range(1, 9)],
        "QT_SIT_TRANCADA": [f"C06{sem}{opt}" for sem in [2, 3] for opt in range(1, 5)],
        "QT_PERDA": [f"C10{motivo}{opt}" for motivo in [1, 2, 3] for opt in range(1, 9)],
        "QT_CONC": [f"C81{sem}{opt}" for sem in range(1, 3) for opt in range(1, 5)] + \
                   [f"C82{grupo}{opt}" for grupo in [1, 2, 3, 4, 5, 7, 8, 10, 11, 12] for opt in range(1, 5)] + \
                   [f"C83{i}" for i in range(1, 9)]
    },
    "SECOMPLE_PRESENCIAL.CSV": {
        "QT_VAGAS": [# Q59.A3 - Vagas/Inscritos/Ingressantes (Nova Questão 2004)
            "C112101", "C112102", "C112201", "C112202","C112301","C112302","C112401","C112402"],
        "QT_ING": [f"C37{faixa:02d}{sexo}" for faixa in range(1, 12) for sexo in range(1, 3)] + \
                  [f"C37{faixa}{sexo}" for faixa in range(12, 23) for sexo in range(1, 3)],
        "QT_MAT": [f"C38{semestre}{sexo_turno}" for semestre in range(1, 3) for sexo_turno in range(1, 5)],
        "QT_SIT_TRANCADA": [f"C1130{grupo}{opt}" for grupo in range(1, 9) for opt in range(1, 5)],
        "QT_CONC": [f"C39{semestre}{sexo}" for semestre in range(1, 3) for sexo in range(1, 5)]
    },
    "SECOMPLE_DISTANCIA.CSV": {
        "QT_VAGAS": ["C117011", "C117021", "C117041", "C117051"],
        "QT_ING": [f"C37{faixa:02d}{sexo}" for faixa in range(1, 12) for sexo in range(1, 3)] + \
                  [f"C37{faixa}{sexo}" for faixa in range(12, 23) for sexo in range(1, 3)],
        "QT_MAT": [f"C38{semestre}{sexo_turno}" for semestre in range(1, 3) for sexo_turno in range(1, 5)],
        "QT_SIT_TRANCADA": [f"C1130{grupo}{opt}" for grupo in range(1, 9) for opt in range(1, 5)],
        "QT_CONC": [f"C39{semestre}{sexo_turno}" for semestre in range(1, 3) for sexo_turno in range(1, 5)]
    }
}

```
