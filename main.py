import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
# from datetime import datetime as dt
import plotly.graph_objects as go

indicadores_nicholsaltierisolo = ["Estrutura", "Compactação e infiltração", "Produndidade do solo",
              "Estado dos resíduos", "Cor, cheiro e matéria orgânica", "Retenção da umidade",
               "Desenvolvimento de raízes", "Cobertura do solo", "Erosão", "Atividade biológica"]

table_header = [
    html.Thead(html.Tr([html.Th("Indicadores"), html.Th("Características")]))
]
row1 =  html.Tr([html.Td("Estrutura"),
                html.Td(
             """(1) Solo empoeirado sem agregados visíveis; 
                (5) Solo solto com poucos agregados que se quebram facilmente;  
                (10) Solo com agregados bem formados, úmidos, difíceis de quebrar.
    """)
    ]
)
row2 =  html.Tr([html.Td("Compactação e infiltração"),
                html.Td(
                    """(1) Compacto, fica inundado;
                    (5) Presença de uma fina camada compacta, a água se infiltra lentamente; 
                    (10) Solo descompactado, a água se infiltra facilmente. 
    """)
    ]
)
row3 = html.Tr([html.Td("Profundidade do solo"),
                html.Td(
                    """(1) Subsolo quase exposto;  
                    (5) Solo superficial fino, com menos de 10cm;
                    (10) Solo superficial mais profundo, com mais de 10cm.
    """)
    ]
)
row4 = html.Tr([html.Td("Estado dos resíduos"),
                html.Td(
                """(1) Presença de resíduos orgânicos que não se decompõe, ou o fazem lentamente;
                (5) Ainda há resíduos do ano anterior em processo de decomposição;
                (10) Resíduos em vários estágios de decomposição, resíduos velhos bem decompostos.
    """)
    ]
)
row5 =  html.Tr([html.Td("Cor, cheiro e matéria orgânica"),
                html.Td(
             """(1) Solo pálido, com cheiro ruim ou químico, não se observa matéria orgânica;
            (5) Solo castanho claro ou avermelhado, com pouco cheiro, e com algum grau de matéria orgânica e húmus;
            (10) Solo de preto à castanho escuro, com cheiro de terra fresca, se observa abundância de matéria orgânica e húmus.
    """)
    ]
)
row6 =  html.Tr([html.Td("Retenção da água (nível de umidade depois da irrigação ou chuva"),
                html.Td(
                    """(1) Solo seca rápido;
                    (5) Solo permanece seco durante a época seca, umidade limitada que se mantém por pouco tempo;
                    (10) Solo mantém a umidade na época seca.

    """)
    ]
)
row7 = html.Tr([html.Td("Desenvolvimento das raízes"),
                html.Td(
                    """(1) Raízes pouco desenvolvidas, adoentadas, e curtas;
                    (5) Raízes com crescimento limitado, se observam algumas raízes finas;
                    (10) Raízes com bom crescimento, saudáveis e profundas, com abundância de raízes finas. 
    """)
    ]
)
row8 = html.Tr([html.Td("Cobertura do solo"),
                html.Td(
                """(1) Solo descoberto;
                (5) Menos da metade do solo coberto por resíduos, folhas e cobertura viva; 
                (10) Mais da metade do solo coberto com cobertura viva e morta. 
    """)
    ]
)
row9 = html.Tr([html.Td("Erosão"),
                html.Td(
                    """(1) Erosão severa, se nota o arraste do solo, presença de sucos e voçorocas;
                    (5) Erosão evidente, mas leve;
                    (10) Sem maiores sinais de erosão. 
    """)
    ]
)
row10 = html.Tr([html.Td("Atividade biológica"),
                html.Td(
                """(1) Sem sinais de atividade biológica, não se observam minhocas ou invertebrados(insetos, aranhas, centopeias, etc.);
                (5) Se observam algumas minhocas e artrópodes;
                (10) Muita atividade biológica e abundância de minhocas e artrópodes.
    """)
    ]
)
table_body = [html.Tbody([row1, row2, row3, row4, row5, row6, row7, row8, row9, row10])]

table = dbc.Table(table_header + table_body, bordered=True)

indi_nicholsaltieri_crop = ['Aparência', 'Crescimento', 'Resistência à estresse',
                                   'Incidência de doenças', 'Competição com espontâneas',
                                   'Rendimento', 'Diversidade genética', 'Diversidade vegetal',
                                   'Diversidade natural circundante', 'Sistema de manejo '
                                   ]
indicadores = indicadores_nicholsaltierisolo

# Initialise the app
app = dash.Dash(
    __name__,
    title='Radar do Solo',
    update_title='Atualizando...',
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)
server = app.server

# Define the app
app.layout = html.Div(
    [
#-------NAVBAR----------------------------------------------------------------------------------------------------------
        dbc.NavbarSimple(
            [

            ],
            sticky='top',
            brand='RADAR DO SOLO',
            color="info",
            dark=True,

        ),

        dbc.Row(html.P()),
        dbc.Row(
            [
                dbc.Col(),
                dbc.Col(
                    [
#-----------------------MANUAL-CARD-------------------------------------------------------------------------------------
                        dbc.Card(
                            [
                                dbc.CardBody(
                                    [
                                        html.H5("MANUAL", className="card-title"),
                                        html.P(
                                            "",
                                            className="card-text",
                                        ),
                                        # dbc.Button(
                                        #     "ESCOLHER", color="info", id="", className="mr-1"
                                        # ),
                                        # dbc.Button(
                                        #     "CRIAR", color="info", id="", className="mr-1"
                                        # ),
                                        html.P(
                                        ),
                                    ]
                                ),
                            ],
                            color='primary',
                            inverse=True
                        ),
                        html.P(),
#-----------------------INDICADORES CARD--------------------------------------------------------------------------------
                        dbc.Card(
                            [
                                dbc.CardBody(
                                    [
                                        html.H5("INDICADORES", className="card-title"),
                                        html.P(
                                            "Escolha indicadores propostos por pesquisadoras(es), ou crie os seus próprios para gerar o radar.",
                                            className="card-text",
                                        ),
                                        dbc.Button(
                                            "ESCOLHER", color="info", id="methods-button", className="mr-1"
                                        ),
                                        dbc.Button(
                                            "CRIAR", color="info", id="new-method-button", className="mr-1"
                                        ),
                                        html.P(
                                        ),
                                    ],
                                ),
                            ],
                            color='primary',
                            inverse=True
                        ),
                        # ESCOLHER INDICADORES
                        dbc.Collapse(
                            [
                                dbc.Card(
                                    dbc.CardBody(
                                        [
                                            dbc.Card(
                                                [
                                                    dbc.CardBody(
                                                        [
                                                            html.H5("SUSTENTABILIDADE DO SOLO",
                                                                    className="card-title"),

                                                            html.P(
                                                                "Método rápido de análise de sustentabilidade do solo, "
                                                                "proposto por NICHOLLS e ALTIERI. Dividido em qualidade"
                                                                " do solo e saúde da collheita."
                                                            ),
                                                            dbc.Button(
                                                                "QUALIDADE DO SOLO", color="dark", id="soil",
                                                                className="mr-1"
                                                            ),
                                                            dbc.Button(
                                                                "SAÚDE DA COLHEITA", color="dark", id="crop",
                                                                className="mr-1"
                                                            ),
                                                            html.P(),

                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    color='primary',
                                ),
                                # SAÚDE DO CULTIVO
                                dbc.Collapse(
                                    [
                                        dbc.Card(
                                            dbc.CardBody(
                                                [
                                                    html.P(''),
                                                    html.H3('Saúde da colheita'),
                                                    html.P(''),
                                                    dbc.Form(
                                                        [
                                                            html.Div(
                                                                'Dê um nome para a análise:'
                                                            ),
                                                            dbc.Input(
                                                                id='name-crop',
                                                                type='text',
                                                                placeholder='Ex: Quintal(colheita)'
                                                            ),
                                                            html.P(''
                                                                   ),
                                                            html.Div(
                                                                indi_nicholsaltieri_crop[
                                                                    0]
                                                            ),
                                                            dbc.Input(
                                                                id='aparencia',
                                                                placeholder='de 1 à 10',
                                                                type='number',
                                                                max=10,
                                                                min=1
                                                            ),
                                                            html.P(''
                                                                   ),
                                                            html.Div(
                                                                indi_nicholsaltieri_crop[
                                                                    1]
                                                            ),
                                                            dbc.Input(
                                                                id='crescimento',
                                                                placeholder='de 1 à 10',
                                                                type='number',
                                                                max=10,
                                                                min=1
                                                            ),
                                                            html.P(''
                                                                   ),
                                                            html.Div(
                                                                indi_nicholsaltieri_crop[
                                                                    2]
                                                            ),
                                                            dbc.Input(
                                                                id='resistencia',
                                                                placeholder='de 1 à 10',
                                                                type='number',
                                                                max=10,
                                                                min=1
                                                            ),
                                                            html.P(''
                                                                   ),
                                                            html.Div(
                                                                indi_nicholsaltieri_crop[
                                                                    3]
                                                            ),
                                                            dbc.Input(
                                                                id='incidencia',
                                                                placeholder='de 1 à 10',
                                                                type='number',
                                                                max=10,
                                                                min=1
                                                            ),
                                                            html.P(''
                                                                   ),
                                                            html.Div(
                                                                indi_nicholsaltieri_crop[
                                                                    4]
                                                            ),
                                                            dbc.Input(
                                                                id='competicao',
                                                                placeholder='de 1 à 10',
                                                                type='number',
                                                                max=10,
                                                                min=1
                                                            ),
                                                            html.P(''
                                                                   ),
                                                            html.Div(
                                                                indi_nicholsaltieri_crop[
                                                                    5]
                                                            ),
                                                            dbc.Input(
                                                                id='rendimento',
                                                                placeholder='de 1 à 10',
                                                                type='number',
                                                                max=10,
                                                                min=1
                                                            ),
                                                            html.P(''
                                                                   ),
                                                            html.Div(
                                                                indi_nicholsaltieri_crop[
                                                                    6]
                                                            ),
                                                            dbc.Input(
                                                                id='genetica',
                                                                placeholder='de 1 à 10',
                                                                type='number',
                                                                max=10,
                                                                min=1
                                                            ),
                                                            html.P(''
                                                                   ),
                                                            html.Div(
                                                                indi_nicholsaltieri_crop[
                                                                    7]
                                                            ),
                                                            dbc.Input(
                                                                id='vegetal',
                                                                placeholder='de 1 à 10',
                                                                type='number',
                                                                max=10,
                                                                min=1
                                                            ),
                                                            html.P(''
                                                                   ),
                                                            html.Div(
                                                                indi_nicholsaltieri_crop[
                                                                    8]
                                                            ),
                                                            dbc.Input(
                                                                id='circundante',
                                                                placeholder='de 1 à 10',
                                                                type='number',
                                                                max=10,
                                                                min=1
                                                            ),
                                                            html.P(''
                                                                   ),
                                                            html.Div(
                                                                indi_nicholsaltieri_crop[
                                                                    9]
                                                            ),
                                                            dbc.Input(
                                                                id='manejo',
                                                                placeholder='de 1 à 10',
                                                                type='number',
                                                                max=10,
                                                                min=1
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            color='light'
                                        ),
                                        dbc.Row(
                                            dbc.Col(
                                                [
                                                    dbc.Card(
                                                        dbc.CardBody(
                                                            [
                                                                dcc.Graph(
                                                                    id='figure-crop'),
                                                            ],
                                                        ),
                                                    ),
                                                ],
                                                width='12',
                                            ),
                                        ),
                                    ],
                                    id='nichols-altieri-crop'
                                ),
                                # QUALIDADE DO SOLO
                                dbc.Collapse(
                                    [
                                        dbc.Card(
                                            dbc.CardBody(
                                                [
                                                    html.P(''),
                                                    html.H2('Qualidade do solo'),
                                                    dbc.Button(
                                                        "Ver manual", color="dark", id="soil-table-button",
                                                        className="mr-1"
                                                    ),
                                                    html.P(),
                                                    dbc.Collapse(
                                                        dbc.Card(
                                                            dbc.CardBody(
                                                                [
                                                                    table
                                                                ]

                                                            ),
                                                            color='light'
                                                        ),
                                                        id='soil-table'
                                                    ),
                                                    html.P(''),
                                                    dbc.Form(
                                                        [
                                                            html.Div(
                                                                'Dê um nome para a análise:'
                                                            ),
                                                            dbc.Input(
                                                                id='name',
                                                                type='text',
                                                                placeholder='Ex: Reforma Agrária já!'
                                                            ),
                                                            html.P(''
                                                                   ),
                                                            html.Div(indicadores[0]
                                                                     ),
                                                            dbc.Input(
                                                                id='ind1',
                                                                placeholder='de 1 à 10',
                                                                type='number',
                                                                max=10,
                                                                min=1
                                                            ),
                                                            html.P(''
                                                                   ),
                                                            html.Div(indicadores[1]
                                                                     ),
                                                            dbc.Input(
                                                                id='ind2',
                                                                placeholder='de 1 à 10',
                                                                type='number',
                                                                max=10,
                                                                min=1
                                                            ),
                                                            html.P(''
                                                                   ),
                                                            html.Div(indicadores[2]
                                                                     ),
                                                            dbc.Input(
                                                                id='ind3',
                                                                placeholder='de 1 à 10',
                                                                type='number',
                                                                max=10,
                                                                min=1
                                                            ),
                                                            html.P(''
                                                                   ),
                                                            html.Div(indicadores[3]
                                                                     ),
                                                            dbc.Input(
                                                                id='ind4',
                                                                placeholder='de 1 à 10',
                                                                type='number',
                                                                max=10,
                                                                min=1
                                                            ),
                                                            html.P(''
                                                                   ),
                                                            html.Div(indicadores[4]
                                                                     ),
                                                            dbc.Input(
                                                                id='ind5',
                                                                placeholder='de 1 à 10',
                                                                type='number',
                                                                max=10,
                                                                min=1
                                                            ),
                                                            html.P(''
                                                                   ),
                                                            html.Div(indicadores[5]
                                                                     ),
                                                            dbc.Input(
                                                                id='ind6',
                                                                placeholder='de 1 à 10',
                                                                type='number',
                                                                max=10,
                                                                min=1
                                                            ),
                                                            html.P(''
                                                                   ),
                                                            html.Div(indicadores[6]
                                                                     ),
                                                            dbc.Input(
                                                                id='ind7',
                                                                placeholder='de 1 à 10',
                                                                type='number',
                                                                max=10,
                                                                min=1
                                                            ),
                                                            html.P(''
                                                                   ),
                                                            html.Div(indicadores[7]
                                                                     ),
                                                            dbc.Input(
                                                                id='ind8',
                                                                placeholder='de 1 à 10',
                                                                type='number',
                                                                max=10,
                                                                min=1
                                                            ),
                                                            html.P(''
                                                                   ),
                                                            html.Div(indicadores[8]
                                                                     ),
                                                            dbc.Input(
                                                                id='ind9',
                                                                placeholder='de 1 à 10',
                                                                type='number',
                                                                max=10,
                                                                min=1
                                                            ),
                                                            html.P(''
                                                                   ),
                                                            html.Div(indicadores[9]
                                                                     ),
                                                            dbc.Input(
                                                                id='ind10',
                                                                placeholder='de 1 à 10',
                                                                type='number',
                                                                max=10,
                                                                min=1
                                                            ),
                                                            html.P(''),
                                                            dbc.Button(
                                                                'GERAR RADAR',
                                                                id='show-soil-radar',
                                                                color='success'
                                                            ),
                                                            html.P(''),
                                                            dbc.Button(
                                                                'ADICIONAR +1 ANÁLISE AO RADAR',
                                                                id='add2-soil',
                                                                color='success'
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            color='light',
                                            inverse=False,
                                        ),
                                        # RADAR DE QUALIDADE DO SOLO 1
                                        dbc.Collapse(
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        dcc.Graph(
                                                            id='figure'
                                                        ),
                                                        html.P(),
                                                    ],
                                                ),
                                            ),
                                            id='soil-radar'
                                        ),
                                        # INPUT DA 2ª ANÁLISE DE QUALIDADE DO SOLO
                                        dbc.Collapse(
                                            [
                                                dbc.Card(
                                                    dbc.CardBody(
                                                        [
                                                            html.P(''),
                                                            html.H2('Qualidade do solo (Análise 2)'),
                                                            html.P(''),
                                                            dbc.Form(
                                                                [
                                                                    html.Div(
                                                                        'Dê um nome para a análise:'
                                                                    ),
                                                                    dbc.Input(
                                                                        id='name-soil2',
                                                                        type='text',
                                                                        placeholder='Ex: Sem Feminismo não há agroecologia!!'
                                                                    ),
                                                                    html.P(''
                                                                           ),
                                                                    html.Div(indicadores[0]
                                                                             ),
                                                                    dbc.Input(
                                                                        id='soil10',
                                                                        placeholder='de 1 à 10',
                                                                        type='number',
                                                                        max=10,
                                                                        min=1
                                                                    ),
                                                                    html.P(''
                                                                           ),
                                                                    html.Div(indicadores[1]
                                                                             ),
                                                                    dbc.Input(
                                                                        id='soil20',
                                                                        placeholder='de 1 à 10',
                                                                        type='number',
                                                                        max=10,
                                                                        min=1
                                                                    ),
                                                                    html.P(''
                                                                           ),
                                                                    html.Div(indicadores[2]
                                                                             ),
                                                                    dbc.Input(
                                                                        id='soil30',
                                                                        placeholder='de 1 à 10',
                                                                        type='number',
                                                                        max=10,
                                                                        min=1
                                                                    ),
                                                                    html.P(''
                                                                           ),
                                                                    html.Div(indicadores[3]
                                                                             ),
                                                                    dbc.Input(
                                                                        id='soil40',
                                                                        placeholder='de 1 à 10',
                                                                        type='number',
                                                                        max=10,
                                                                        min=1
                                                                    ),
                                                                    html.P(''
                                                                           ),
                                                                    html.Div(indicadores[4]
                                                                             ),
                                                                    dbc.Input(
                                                                        id='soil50',
                                                                        placeholder='de 1 à 10',
                                                                        type='number',
                                                                        max=10,
                                                                        min=1
                                                                    ),
                                                                    html.P(''
                                                                           ),
                                                                    html.Div(indicadores[5]
                                                                             ),
                                                                    dbc.Input(
                                                                        id='soil60',
                                                                        placeholder='de 1 à 10',
                                                                        type='number',
                                                                        max=10,
                                                                        min=1
                                                                    ),
                                                                    html.P(''
                                                                           ),
                                                                    html.Div(indicadores[6]
                                                                             ),
                                                                    dbc.Input(
                                                                        id='soil70',
                                                                        placeholder='de 1 à 10',
                                                                        type='number',
                                                                        max=10,
                                                                        min=1
                                                                    ),
                                                                    html.P(''
                                                                           ),
                                                                    html.Div(indicadores[7]
                                                                             ),
                                                                    dbc.Input(
                                                                        id='soil80',
                                                                        placeholder='de 1 à 10',
                                                                        type='number',
                                                                        max=10,
                                                                        min=1
                                                                    ),
                                                                    html.P(''
                                                                           ),
                                                                    html.Div(indicadores[8]
                                                                             ),
                                                                    dbc.Input(
                                                                        id='soil90',
                                                                        placeholder='de 1 à 10',
                                                                        type='number',
                                                                        max=10,
                                                                        min=1
                                                                    ),
                                                                    html.P(''
                                                                           ),
                                                                    html.Div(indicadores[9]
                                                                             ),
                                                                    dbc.Input(
                                                                        id='soil100',
                                                                        placeholder='de 1 à 10',
                                                                        type='number',
                                                                        max=10,
                                                                        min=1
                                                                    ),
                                                                    html.P(''),
                                                                    dbc.Button(
                                                                        'GERAR RADAR',
                                                                        id='show-soil-radar2',
                                                                        color='success'
                                                                    ),
                                                                    html.P(''),
                                                                    dbc.Button(
                                                                        'ADICIONAR +1 ANÁLISE AO RADAR',
                                                                        id='add3-soil',
                                                                        color='success'
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    color='light',
                                                    inverse=False,
                                                ),
                                                dbc.Collapse(
                                                    dbc.Card(
                                                        dbc.CardBody(
                                                            [
                                                                dcc.Graph(
                                                                    id='fig-soil-2'
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    id='soil-radar2'
                                                ),
                                            ],
                                            id='soil-2'
                                        ),

                                    ],
                                    id='nichols-altieri-soil'
                                ),
                            ],
                            id="methods",
                        ),
                        # CRIAR INDICADORES
                        dbc.Collapse(
                            [
                                dbc.Card(
                                    dbc.CardBody(
                                        [
                                            dbc.FormGroup(
                                                [
                                                    html.P(),
                                                    html.H3('Crie seus próprios indicadores:'),
                                                    html.P(),
                                                    html.Div('Dê um nome para seu método:'),
                                                    dbc.Input(type="text", id="new-method-name",
                                                              placeholder="Ex: Método Solo Sadio (Associação do BioPoder Campones)"),
                                                    html.P(),
                                                    dbc.Input(type="text", id="cria1",
                                                              placeholder="Indicador 1"),
                                                    html.P(),
                                                    dbc.Input(type="text", id="cria2",
                                                              placeholder="Indicador 2"),
                                                    html.P(),
                                                    dbc.Input(type="text", id="cria3",
                                                              placeholder="Indicador 3",),
                                                    html.P(),
                                                    dbc.Input(type="text", id="cria4",
                                                              placeholder="Indicador 4"),
                                                    html.P(),
                                                    dbc.Input(type="text", id="cria5",
                                                              placeholder="Indicador 5"),
                                                    html.P(),
                                                    dbc.Input(type="text", id="cria6",
                                                              placeholder="Indicador 6"),
                                                    html.P(),
                                                    dbc.Input(type="text", id="cria7",
                                                              placeholder="Indicador 7"),
                                                    html.P(),
                                                    dbc.Input(type="text", id="cria8",
                                                              placeholder="Indicador 8"),
                                                    html.P(),
                                                    dbc.Input(type="text", id="cria9",
                                                              placeholder="Indicador 9"),
                                                    html.P(),
                                                    dbc.Input(type="text", id="cria10",
                                                              placeholder="Indicador 10"),
                                                    html.P(),
                                                    dbc.Button('PRONTO', color='success', id='save-new-method'),
                                                ]
                                            ),
                                        ],
                                    ),
                                    color='primary',
                                    inverse=True,
                                ),
                                # ANÁLISE PERSONALIZADA
                                dbc.Collapse(
                                    [
                                        dbc.Card(
                                            dbc.CardBody(
                                                [
                                                    dbc.Form(
                                                        [
                                                            html.P(),
                                                            html.H3(id='method-name'),
                                                            html.P(),
                                                            html.Div(
                                                                'Dê um nome para essa análise:'
                                                            ),
                                                            dbc.Input(
                                                                id='name_new',
                                                                type='text',
                                                                placeholder='Ex: Pasto(03/03/2023)'
                                                            ),
                                                            html.P(''
                                                                   ),
                                                            html.Div(
                                                                id='new-1-out'
                                                            ),
                                                            dbc.Input(
                                                                id='new1',
                                                                placeholder='de 1 à 10',
                                                                type='number',
                                                                max=10,
                                                                min=1
                                                            ),
                                                            html.P(''
                                                                   ),
                                                            html.Div(
                                                                id='new-2-out'
                                                            ),
                                                            dbc.Input(
                                                                id='new2',
                                                                placeholder='de 1 à 10',
                                                                type='number',
                                                                max=10,
                                                                min=1
                                                            ),
                                                            html.P(''
                                                                   ),
                                                            html.Div(
                                                                id='new-3-out'
                                                            ),
                                                            dbc.Input(
                                                                id='new3',
                                                                placeholder='de 1 à 10',
                                                                type='number',
                                                                max=10,
                                                                min=1
                                                            ),
                                                            html.P(''
                                                                   ),
                                                            html.Div(
                                                                id='new-4-out'
                                                            ),
                                                            dbc.Input(
                                                                id='new4',
                                                                placeholder='de 1 à 10',
                                                                type='number',
                                                                max=10,
                                                                min=1
                                                            ),
                                                            html.P(''
                                                                   ),
                                                            html.Div(
                                                                id='new-5-out'
                                                            ),
                                                            dbc.Input(
                                                                id='new5',
                                                                placeholder='de 1 à 10',
                                                                type='number',
                                                                max=10,
                                                                min=1
                                                            ),
                                                            html.P(''
                                                                   ),
                                                            html.Div(
                                                                id='new-6-out'
                                                            ),
                                                            dbc.Input(
                                                                id='new6',
                                                                placeholder='de 1 à 10',
                                                                type='number',
                                                                max=10,
                                                                min=1
                                                            ),
                                                            html.P(''
                                                                   ),
                                                            html.Div(
                                                                id='new-7-out'
                                                            ),
                                                            dbc.Input(
                                                                id='new7',
                                                                placeholder='de 1 à 10',
                                                                type='number',
                                                                max=10,
                                                                min=1
                                                            ),
                                                            html.P(''
                                                                   ),
                                                            html.Div(
                                                                id='new-8-out'
                                                            ),
                                                            dbc.Input(
                                                                id='new8',
                                                                placeholder='de 1 à 10',
                                                                type='number',
                                                                max=10,
                                                                min=1
                                                            ),
                                                            html.P(''
                                                                   ),
                                                            html.Div(
                                                                id='new-9-out'
                                                            ),
                                                            dbc.Input(
                                                                id='new9',
                                                                placeholder='de 1 à 10',
                                                                type='number',
                                                                max=10,
                                                                min=1
                                                            ),
                                                            html.P(''
                                                                   ),
                                                            html.Div(
                                                                id='new-10-out'
                                                            ),
                                                            dbc.Input(
                                                                id='new10',
                                                                placeholder='de 1 à 10',
                                                                type='number',
                                                                max=10,
                                                                min=1
                                                            ),
                                                            html.P(),
                                                            dbc.Button('GERAR RADAR', color='success',
                                                                       id='show-new-radar'),
                                                            html.P(),
                                                            dbc.Button('ADICIONAR +1 ANÁLISE AO RADAR', color='success',
                                                                       id='add-new-method2'),
                                                        ],
                                                    ),
                                                ]
                                            ),
                                        ),
                                        dbc.Collapse(
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        dcc.Graph(
                                                            id='figure-new'),
                                                    ],
                                                ),
                                            ),
                                            id='new-radar'
                                        ),
                                    ],
                                    id='maked-method'
                                ),
                                # ANÁLISE PERSONALIZADA 2
                                dbc.Collapse(
                                    [
                                        dbc.Card(
                                            dbc.CardBody(
                                                [
                                                    dbc.Form(
                                                        [
                                                            html.P(),
                                                            html.H3(id='method-name2'),
                                                            html.P(),
                                                            html.Div('Dê um nome para essa análise:'),
                                                            dbc.Input(
                                                                id='name_new2',
                                                                type='text',
                                                                placeholder='Ex: Pasto(03/03/2023)'
                                                            ),
                                                            html.P(''),
                                                            html.Div(
                                                                id='2new-1-out'
                                                            ),
                                                            dbc.Input(
                                                                id='2new1',
                                                                placeholder='de 1 à 10',
                                                                type='number',
                                                                max=10,
                                                                min=1
                                                            ),
                                                            html.P(''
                                                                   ),
                                                            html.Div(
                                                                id='2new-2-out'
                                                            ),
                                                            dbc.Input(
                                                                id='2new2',
                                                                placeholder='de 1 à 10',
                                                                type='number',
                                                                max=10,
                                                                min=1
                                                            ),
                                                            html.P(''
                                                                   ),
                                                            html.Div(
                                                                id='2new-3-out'
                                                            ),
                                                            dbc.Input(
                                                                id='2new3',
                                                                placeholder='de 1 à 10',
                                                                type='number',
                                                                max=10,
                                                                min=1
                                                            ),
                                                            html.P(''
                                                                   ),
                                                            html.Div(
                                                                id='2new-4-out'
                                                            ),
                                                            dbc.Input(
                                                                id='2new4',
                                                                placeholder='de 1 à 10',
                                                                type='number',
                                                                max=10,
                                                                min=1
                                                            ),
                                                            html.P(''
                                                                   ),
                                                            html.Div(
                                                                id='2new-5-out'
                                                            ),
                                                            dbc.Input(
                                                                id='2new5',
                                                                placeholder='de 1 à 10',
                                                                type='number',
                                                                max=10,
                                                                min=1
                                                            ),
                                                            html.P(''
                                                                   ),
                                                            html.Div(
                                                                id='2new-6-out'
                                                            ),
                                                            dbc.Input(
                                                                id='2new6',
                                                                placeholder='de 1 à 10',
                                                                type='number',
                                                                max=10,
                                                                min=1
                                                            ),
                                                            html.P(''
                                                                   ),
                                                            html.Div(
                                                                id='2new-7-out'
                                                            ),
                                                            dbc.Input(
                                                                id='2new7',
                                                                placeholder='de 1 à 10',
                                                                type='number',
                                                                max=10,
                                                                min=1
                                                            ),
                                                            html.P(''
                                                                   ),
                                                            html.Div(
                                                                id='2new-8-out'
                                                            ),
                                                            dbc.Input(
                                                                id='2new8',
                                                                placeholder='de 1 à 10',
                                                                type='number',
                                                                max=10,
                                                                min=1
                                                            ),
                                                            html.P(''
                                                                   ),
                                                            html.Div(
                                                                id='2new-9-out'
                                                            ),
                                                            dbc.Input(
                                                                id='2new9',
                                                                placeholder='de 1 à 10',
                                                                type='number',
                                                                max=10,
                                                                min=1
                                                            ),
                                                            html.P(''
                                                                   ),
                                                            html.Div(
                                                                id='2new-10-out'
                                                            ),
                                                            dbc.Input(
                                                                id='2new10',
                                                                placeholder='de 1 à 10',
                                                                type='number',
                                                                max=10,
                                                                min=1
                                                            ),
                                                            html.P(),
                                                            dbc.Button('GERAR RADAR', color='success',
                                                                       id='show-new-radar2'
                                                            ),
                                                            html.P(),
                                                            dbc.Button('ADICIONAR +1 ANÁLISE AO RADAR', color='success',
                                                                       id='add-new-method3'
                                                            ),
                                                        ],
                                                    ),
                                                ]
                                            ),
                                        ),
                                        dbc.Collapse(
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                        dcc.Graph(
                                                            id='figure2-new'),
                                                    ],
                                                ),
                                            ),
                                            id='new-radar2'
                                        ),
                                    ],
                                    id='maked2-method'
                                ),

                            ],
                            id="new-method",
                        ),
                    ],
    #---------------TAMANHO DO CARD INDICADORES
                    width='auto',
                ),
                dbc.Col(),
            ],
        ),
        dbc.Row(
            html.P(

            ),
        ),
        # CARD DE INFORMAÇÕES
        dbc.Row(
            dbc.Col(
                [
                    dbc.Card(
                        dbc.CardBody(
                            [

                                html.H6('Apoie o Radar do Solo: '),
                                dbc.Badge("Apoia.se", href="#", color="primary"),
                                html.P(''),
                                html.H6('Colabore no código do projeto: '),
                                dbc.Badge("GitHub", href="https://github.com/serenozin/RadarDoSolo", color="primary"),
                                html.P(''),
                                html.H6('Desenvolvido por Patryck Harley'),
                                dbc.Badge('patryck@outlook.com', color='primary'),

                            ]
                        ),
                        color='info',
                        inverse=True,
                    )
                ],
            ),
        )
    ],
)
#--------------------------------------------------------------------CALLBACKS------------------------------------------
# ABRIR ÁREA DE ESCOLHA DE INDICADORES
@app.callback(
    Output('methods', 'is_open'),
    [Input("methods-button", "n_clicks")],
    [State("methods", "is_open")],
)
def open_methods(n, is_open):
    if n:
        return not is_open
    return is_open

# ABRIR ÁREA DE CRIAÇÃO DE INDICADORES
@app.callback(
    Output('new-method', 'is_open'),
    [Input("new-method-button", "n_clicks")],
    [State("new-method", "is_open")],
)
def open_new_method(n, is_open):
    if n:
        return not is_open
    return is_open

# ABRIR ÁREA DE GERAR RADAR PERSONALIZADO
@app.callback(
    Output('maked-method', 'is_open'),
    [Input("save-new-method", "n_clicks")],
    [State("maked-method", "is_open")],
)
def open_maked_method(n, is_open):
    if n:
        return not is_open
    return is_open
# ABRIR RADAR PERSONALIZADO
@app.callback(
    Output('new-radar', 'is_open'),
    [Input("show-new-radar", "n_clicks")],
    [State("new-radar", "is_open")],
)
def open_maked_method(n, is_open):
    if n:
        return not is_open
    return is_open

# ABRIR RADAR PERSONALIZADO 2
@app.callback(
    Output('new-radar2', 'is_open'),
    [Input("show-new-radar2", "n_clicks")],
    [State("new-radar2", "is_open")],
)
def open_maked_method(n, is_open):
    if n:
        return not is_open
    return is_open

# ABRIR ÁREA DE GERAR RADAR PERSONALIZADO 2
@app.callback(
    Output('maked2-method', 'is_open'),
    [Input("add-new-method2", "n_clicks")],
    [State("maked2-method", "is_open")],
)
def open_maked_method(n, is_open):
    if n:
        return not is_open
    return is_open

# ABRIR ÁREA GERAR RADAR DE NICHOLS E ALTIERI QUALIDADE DO SOLO
@app.callback(
    Output('nichols-altieri-soil', 'is_open'),
    [Input("soil", "n_clicks")],
    [State("nichols-altieri-soil", "is_open")],
)
def open_soil(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output('soil-table', 'is_open'),
    [Input("soil-table-button", "n_clicks")],
    [State("soil-table", "is_open")],
)
def open_soil_table(n, is_open):
    if n:
        return not is_open
    return is_open

# ABRIR ÁREA GERAR RADAR DE NICHOLS E ALTIERI SAUDE DA COLHEITA
@app.callback(
    Output('nichols-altieri-crop', 'is_open'),
    [Input("crop", "n_clicks")],
    [State("nichols-altieri-crop", "is_open")],
)
def open_crop(n, is_open):
    if n:
        return not is_open
    return is_open

# ABRIR RADAR DE QUALIDADE DO SOLO
@app.callback(
    Output('soil-radar', 'is_open'),
    [Input("show-soil-radar", "n_clicks")],
    [State("soil-radar", "is_open")],
)
def open_crop(n, is_open):
    if n:
        return not is_open
    return is_open

# ABRIR RADAR DE QUALIDADE DO SOLO 2
@app.callback(
    Output('soil-radar2', 'is_open'),
    [Input("show-soil-radar2", "n_clicks")],
    [State("soil-radar2", "is_open")],
)
def open_crop(n, is_open):
    if n:
        return not is_open
    return is_open

# ÁREA DA 2ª ANALISE DE QUALIDADE DO SOLO
@app.callback(
    Output('soil-2', 'is_open'),
    [Input("add2-soil", "n_clicks")],
    [State("soil-2", "is_open")],
)
def open_crop(n, is_open):
    if n:
        return not is_open
    return is_open

# ATUALIZAR INDICADORES PERSONALIZADOS
@app.callback(
    [Output('method-name', 'children'),
     Output('method-name2', 'children')],
    [Input('new-method-name', 'value')]
)
def update_new_output(input_value):
    return '{}'.format(input_value), '{} (Análise 2)'.format(input_value)

@app.callback(
    [Output('new-1-out', 'children'),
    Output('2new-1-out', 'children')],
    [Input('cria1', 'value')]
)
def update_new_output(input_value):
    return '{}: '.format(input_value), '{}: '.format(input_value)

@app.callback(
    [Output('new-2-out', 'children'),
     Output('2new-2-out', 'children')],
    [Input('cria2', 'value')]
)
def update_new_output(input_value):
    return '{}: '.format(input_value), '{}: '.format(input_value)

@app.callback(
    [Output('new-3-out', 'children'),
     Output('2new-3-out', 'children')],
    [Input('cria3', 'value')]
)
def update_new_output(input_value):
    return '{}: '.format(input_value), '{}: '.format(input_value)

@app.callback(
    [Output('new-4-out', 'children'),
     Output('2new-4-out', 'children')],
    [Input('cria4', 'value')]
)
def update_new_output(input_value):
    return '{}: '.format(input_value), '{}: '.format(input_value)

@app.callback(
    [Output('new-5-out', 'children'),
     Output('2new-5-out', 'children')],
    [Input('cria5', 'value')]
)
def update_new_output(input_value):
    return '{}: '.format(input_value), '{}: '.format(input_value)

@app.callback(
    [Output('new-6-out', 'children'),
     Output('2new-6-out', 'children')],
    [Input('cria6', 'value')]
)
def update_new_output(input_value):
    return '{}: '.format(input_value), '{}: '.format(input_value)

@app.callback(
    [Output('new-7-out', 'children'),
     Output('2new-7-out', 'children')],
    [Input('cria7', 'value')]
)
def update_new_output(input_value):
    return '{}: '.format(input_value), '{}: '.format(input_value)

@app.callback(
    [Output('new-8-out', 'children'),
     Output('2new-8-out', 'children')],
    [Input('cria8', 'value')]
)
def update_new_output(input_value):
    return '{}: '.format(input_value), '{}: '.format(input_value)

@app.callback(
    [Output('new-9-out', 'children'),
     Output('2new-9-out', 'children')],
    [Input('cria9', 'value')]
)
def update_new_output(input_value):
    return '{}: '.format(input_value), '{}: '.format(input_value)

@app.callback(
    [Output('new-10-out', 'children'),
    Output('2new-10-out', 'children')],
    [Input('cria10', 'value')]
)
def update_new_output(input_value):
    return '{}: '.format(input_value), '{}: '.format(input_value)



# ATUALIZAR RADAR DE QUALIDADE DO SOLO
@app.callback(
    Output('figure', 'figure'),
    [Input('name', 'value'),
     Input('ind1', 'value'),
     Input('ind2', 'value'),
     Input('ind3', 'value'),
     Input('ind4', 'value'),
     Input('ind5', 'value'),
     Input('ind6', 'value'),
     Input('ind7', 'value'),
     Input('ind8', 'value'),
     Input('ind9', 'value'),
     Input('ind10', 'value'),
     ]
)
def chart_soil_update (name_value, ind1_value, ind2_value, ind3_value, ind4_value, ind5_value, ind6_value,
                       ind7_value, ind8_value, ind9_value, ind10_value,
                       ):
    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=[ind1_value, ind2_value, ind3_value, ind4_value, ind5_value,
           ind6_value, ind7_value, ind8_value, ind9_value, ind10_value
           ],
        theta=indicadores,
        fill='toself',
        name= name_value,
    ))


    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10]
            ),
        ),
        showlegend=True
    )

    return fig

@app.callback(
    Output('fig-soil-2', 'figure'),
    [Input('name', 'value'),
     Input('ind1', 'value'),
     Input('ind2', 'value'),
     Input('ind3', 'value'),
     Input('ind4', 'value'),
     Input('ind5', 'value'),
     Input('ind6', 'value'),
     Input('ind7', 'value'),
     Input('ind8', 'value'),
     Input('ind9', 'value'),
     Input('ind10', 'value'),
     Input('name-soil2', 'value'),
      Input('soil10', 'value'),
      Input('soil20', 'value'),
      Input('soil30', 'value'),
      Input('soil40', 'value'),
      Input('soil50', 'value'),
      Input('soil60', 'value'),
      Input('soil70', 'value'),
      Input('soil80', 'value'),
      Input('soil90', 'value'),
      Input('soil100', 'value'),
    ]
)

def add_analise (name_value, ind1_value, ind2_value, ind3_value, ind4_value, ind5_value, ind6_value,
                        ind7_value, ind8_value, ind9_value, ind10_value,
                        name_soil2, soil1_value, soil2_value, soil3_value, soil4_value, soil5_value,
                        soil6_value, soil7_value, soil8_value, soil9_value, soil10_value):

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=[ind1_value, ind2_value, ind3_value, ind4_value, ind5_value,
           ind6_value, ind7_value, ind8_value, ind9_value, ind10_value
           ],
        theta=indicadores,
        fill='toself',
        name= name_value,
    ))

    fig.add_trace(go.Scatterpolar(
        r=[soil1_value, soil2_value, soil3_value, soil4_value, soil5_value,
            soil6_value, soil7_value, soil8_value, soil9_value, soil10_value],
        theta=indicadores,
        fill='toself',
        name=name_soil2
    ))
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10]
            ),
        ),
        showlegend=True
    )
    return fig
# ATUALIZAR RADAR SAUDE DA COLHEITA
@app.callback(
    Output('figure-crop', 'figure'),
    [Input('name-crop', 'value'),
     Input('aparencia', 'value'),
     Input('crescimento', 'value'),
     Input('resistencia', 'value'),
     Input('incidencia', 'value'),
     Input('competicao', 'value'),
     Input('rendimento', 'value'),
     Input('genetica', 'value'),
     Input('vegetal', 'value'),
     Input('circundante', 'value'),
     Input('manejo', 'value'),
     ]
)
def chart_crop_update (name_value, aparencia, crescimento, resistencia, incidencia, competicao, rendimento,
                  genetica, vegetal, circundante, manejo):

    fig = go.Figure(data=go.Scatterpolar(
        name= name_value,
        r=[aparencia, crescimento, resistencia, incidencia, competicao,
           rendimento, genetica, vegetal, circundante, manejo
           ],
        theta=indi_nicholsaltieri_crop,
        fill='toself',

    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10]
            ),
        ),
        showlegend=True
    )

    return fig

# ATUALIZAR RADAR PERSONALIZADO
@app.callback(
    Output('figure-new', 'figure'),
    [Input('name_new', 'value'),
     Input('new1', 'value'),
     Input('new2', 'value'),
     Input('new3', 'value'),
     Input('new4', 'value'),
     Input('new5', 'value'),
     Input('new6', 'value'),
     Input('new7', 'value'),
     Input('new8', 'value'),
     Input('new9', 'value'),
     Input('new10', 'value'),
     Input('cria1', 'value'),
     Input('cria2', 'value'),
     Input('cria3', 'value'),
     Input('cria4', 'value'),
     Input('cria5', 'value'),
     Input('cria6', 'value'),
     Input('cria7', 'value'),
     Input('cria8', 'value'),
     Input('cria9', 'value'),
     Input('cria10', 'value'),
     ]
)
def chart_crop_update (name_new, new1, new2, new3, new4, new5, new6, new7, new8, new9, new10,
                       out1, out2, out3, out4, out5, out6, out7, out8, out9, out10):

    fig = go.Figure(data=go.Scatterpolar(
        name= name_new,
        r=[new1, new2, new3, new4, new5,
           new6, new7, new8, new9, new10
           ],
        theta=[out1, out2, out3, out4, out5, out6, out7, out8, out9, out10],
        fill='toself',

    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10]
            ),
        ),
        showlegend=True
    )

    return fig

# ATUALIZAR RADAR PERSONALZIADO 2
@app.callback(
    Output('figure2-new', 'figure'),
    [Input('name_new', 'value'),
     Input('new1', 'value'),
     Input('new2', 'value'),
     Input('new3', 'value'),
     Input('new4', 'value'),
     Input('new5', 'value'),
     Input('new6', 'value'),
     Input('new7', 'value'),
     Input('new8', 'value'),
     Input('new9', 'value'),
     Input('new10', 'value'),
     Input('name_new2', 'value'),
     Input('2new1', 'value'),
     Input('2new2', 'value'),
     Input('2new3', 'value'),
     Input('2new4', 'value'),
     Input('2new5', 'value'),
     Input('2new6', 'value'),
     Input('2new7', 'value'),
     Input('2new8', 'value'),
     Input('2new9', 'value'),
     Input('2new10', 'value'),
     Input('cria1', 'value'),
     Input('cria2', 'value'),
     Input('cria3', 'value'),
     Input('cria4', 'value'),
     Input('cria5', 'value'),
     Input('cria6', 'value'),
     Input('cria7', 'value'),
     Input('cria8', 'value'),
     Input('cria9', 'value'),
     Input('cria10', 'value'),
     ]
)
def chart_crop_update (name_new, new1, new2, new3, new4, new5, new6, new7, new8, new9, new10,
                       name_new2, new210, new20, new30, new40, new50, new60, new70, new80, new90, new100,
                       out1, out2, out3, out4, out5, out6, out7, out8, out9, out10):

    fig = go.Figure(data=go.Scatterpolar(
        name= name_new,
        r=[
           ],
        theta=[],
        fill='toself',

    ))
    fig.add_trace(go.Scatterpolar(
        r=[new1, new2, new3, new4, new5,
           new6, new7, new8, new9, new10
           ],
        theta=[out1, out2, out3, out4, out5, out6, out7, out8, out9, out10],
        fill='toself',
        name= name_new,
    ))
    fig.add_trace(go.Scatterpolar(
        r=[new210, new20, new30, new40, new50,
           new60, new70, new80, new90, new100
           ],
        theta=[out1, out2, out3, out4, out5, out6, out7, out8, out9, out10],
        fill='toself',
        name= name_new2,
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10]
            ),
        ),
        showlegend=True
    )

    return fig
# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)