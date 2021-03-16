import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
# from datetime import datetime as dt
import plotly.graph_objects as go

#-----------------------------------TABELAS-----------------------------------------------------------------------------
table_header2 = [
    html.Thead(html.Tr([html.Th("Indicadores"), html.Th("(Valores correspondentes) Características*")]))
]
row12 =  html.Tr([html.Td("Aparência"),
                html.Td(
             """(1)Cultivo com clorose ou descolorido, com sinais severos de deficiência de nutrientes;
                (5) Cultivo verde claro, com algumas descolorações; 
                (10) Folhagem verde intenso, sem sinais de deficiência. 

    """)
    ]
)
row22 =  html.Tr([html.Td("Crescimento do cultivo"),
                html.Td(
                    """(1) Cultivo pouco denso, de crescimento pobre. Talos e ramos curtos e quebradiços; 
                        (5) Cultivo mais denso, mas não uniforme, com crescimento novo  e com ramos e talos ainda finos;  
                        (10) Cultivo denso, uniforme, bom crescimento, com ramas e talos grossos e firmes. 

    """)
    ]
)
row32 = html.Tr([html.Td("Resistência ou tolerância à estresse"),
                html.Td(
                    """(1) Suscetíveis, não se recuperam bem depois de um estresse;
                        (5) Sofrem em época seca ou muito chuvosa, se recuperam lentamente;
                        (10) Suportam secas e chuvas intensas, recuperação rápida.

    """)
    ]
)
row42 = html.Tr([html.Td("Incidência de doenças"),
                html.Td(
                """(1) Suscetível à doenças, mais de 50% de plantas com sintomas; 
                    (5) Entre 20-45% de plantas com sintomas de leves à severos;
                    (10) Resistentes, menos de 20% de plantas com sintomas leves. 

    """)
    ]
)
row52 =  html.Tr([html.Td("Competição com espontâneas"),
                html.Td(
             """(1) Cultivos estressados dominados por espontâneas;
                (5) Presença média de espontâneas, cultivo sofre competição; 
                (10) Cultivo vigoroso, se sobrepõe às espontâneas, ou elas não causam problema.

    """)
    ]
)
row62 =  html.Tr([html.Td("Rendimento atual ou potencial"),
                html.Td(
                    """(1) Baixo, em relação à media da área;
                        (5) Médio, aceitável em relação à média da área;
                        (10) Bom ou alto, em relação à média da área. 


    """)
    ]
)
row72 = html.Tr([html.Td("Diversidade genética**"),
                html.Td(
                    """(1) Pobre, domina apenas uma variedade de cultivo;
                        (5) Média, duas variedades;
                        (10) Alta, mais de duas variedades. 

    """)
    ]
)
row82 = html.Tr([html.Td("Diversidade vegetal"),
                html.Td(
                """(1) Monocultivo sem sombra;
                    (5) Com apenas uma espécie de sombra;
                    (10) Com mais de duas espécies de sombra, e até mesmo outras culturas ou espontâneas dominantes. 

    """)
    ]
)
row92 = html.Tr([html.Td("Diversidade natural circundante"),
                html.Td(
                    """(1) Rodeado por outros cultivos, campos abertos ou estradas;
                        (5) Rodeado ao menos em um lado por vegetação natural;
                        (10) Rodeado ao menos em 50% de suas bordas por vegetação natural.

    """)
    ]
)
row102 = html.Tr([html.Td("Sistema de manejo"),
                html.Td("""(1) Monocultivo convencional, com manejado com agroquímicos;
                            (5) Em transição ao orgânico, com substituição de insumos;
                            (10) Orgânico diversificado, com pouco uso de insumos orgânicos ou biológicos."""
                ),
    ]
)
row112 = html.Tr(html.Td("""* As características foram pensadas para o cultivo 
de café no trabalho de Nicholls e Altieri, adapte ao cultivo que deseja analisar.
** Embora a presença de um maior número de variedades de café signifique 
maior diversidade genética, pode ser que algumas dessas variedades sejam 
altamente suscetíveis a um determinado patógeno ou que a qualidade de 
algumas para beber não seja boa ou tenha algumas características indesejáveis."""),
)
table_body2 = [html.Tbody([row12, row22, row32, row42, row52, row62, row72, row82, row92, row102, row112])]

table2 = dbc.Table(table_header2 + table_body2, bordered=True)




table_header = [
    html.Thead(html.Tr([html.Th("Indicadores"), html.Th("(Valores correspondentes)Características")]))
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

indicadores_nichollsaltieri_soil = ["Estrutura", "Compactação e infiltração", "Produndidade do solo",
              "Estado dos resíduos", "Cor, cheiro e matéria orgânica", "Retenção da umidade",
               "Desenvolvimento de raízes", "Cobertura do solo", "Erosão", "Atividade biológica"]

indi_nicholsaltieri_crop = ['Aparência: ', 'Crescimento: ', 'Resistência à estresse: ',
                                   'Incidência de doenças: ', 'Competição com espontâneas: ',
                                   'Rendimento: ', 'Diversidade genética: ', 'Diversidade vegetal: ',
                                   'Diversidade natural circundante: ', 'Sistema de manejo: '
                                   ]
indicadores = ["Estrutura: ", "Compactação e infiltração: ", "Produndidade do solo: ",
              "Estado dos resíduos: ", "Cor, cheiro e matéria orgânica: ", "Retenção da umidade: ",
               "Desenvolvimento de raízes: ", "Cobertura do solo: ", "Erosão: ", "Atividade biológica: "]

indi_crop = ['Aparência', 'Crescimento', 'Resistência à estresse',
                                   'Incidência de doenças', 'Competição com espontâneas',
                                   'Rendimento', 'Diversidade genética', 'Diversidade vegetal',
                                   'Diversidade natural circundante', 'Sistema de manejo '
                                   ]
def radar_chart(
    name1, name2 = None, name3 = None, name4 = None, name5 = None,
    r1 = None, r2 = None, r3 = None, r4 = None, r5 = None,
    theta = None,
    title = None
    ):

    theta.append(theta[0])

    fig = go.Figure()
    fig.update_layout(title=title)

    if r2 == None and r3 == None and r4 == None and r5 == None: 
        r1.append(r1[0])
        fig.add_trace(go.Scatterpolar(
            r=r1, theta=theta,
            name=name1,
            )
        )
    elif r3 == None and r4 == None and r5 == None:
        r1.append(r1[0])
        r2.append(r2[0])
        fig.add_trace(go.Scatterpolar(
            r=r1, theta=theta,
            name=name1,
            )
        )
        fig.add_trace(go.Scatterpolar(
            r=r2, theta=theta,
            name=name2,
            )
        )

    elif r4 == None and r5 == None:
        r1.append(r1[0])
        r2.append(r2[0])
        r3.append(r3[0])
        fig.add_trace(go.Scatterpolar(
            r=r1, theta=theta,
            name=name1,
            )
        )
        fig.add_trace(go.Scatterpolar(
            r=r2, theta=theta,
            name=name2,
            )
        )
        fig.add_trace(go.Scatterpolar(
            r=r3, theta=theta,
            name=name3,
            )
        )
    elif r5 == None:
        r1.append(r1[0])
        r2.append(r2[0])
        r3.append(r3[0])
        r4.append(r4[0])
        fig.add_trace(go.Scatterpolar(
            r=r1, theta=theta,
            name=name1,
            )
        )
        fig.add_trace(go.Scatterpolar(
            r=r2, theta=theta,
            name=name2,
            )
        )
        fig.add_trace(go.Scatterpolar(
            r=r3, theta=theta,
            name=name3,
            )
        )
        fig.add_trace(go.Scatterpolar(
            r=r4, theta=theta,
            name=name4,
            )
        )
    else:
        r1.append(r1[0])
        r2.append(r2[0])
        r3.append(r3[0])
        r4.append(r4[0])
        r5.append(r5[0])
        fig.add_trace(go.Scatterpolar(
            r=r1, theta=theta,
            name=name1,
            )
        )
        fig.add_trace(go.Scatterpolar(
            r=r2, theta=theta,
            name=name2,
            )
        )
        fig.add_trace(go.Scatterpolar(
            r=r3, theta=theta,
            name=name3,
            )
        )
        fig.add_trace(go.Scatterpolar(
            r=r4, theta=theta,
            name=name4,
            )
        )
        fig.add_trace(go.Scatterpolar(
            r=r5, theta=theta,
            name=name5,
            )
        )

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
                        dbc.Toast(
                            [html.P("Agora o gráfico suporta até 5 análises!", className="mb-0")],
                            header="Atualização 1.2",
                            dismissable=True,
                        ),
                        dbc.Card(
                            [
                                dbc.CardBody(
                                    [
                                        html.H5("VISUALIZAÇÃO INTERATIVA DE INDICADORES."),
                                        html.P(''),
                                        dbc.CardImg(src="/assets/exemplo.png", bottom=False),
                                        html.P(
                                            'Para baixar uma imagem do radar como essa acima é só clicar no ícone de câmera, no gráfico da sua análise'),
                                    ],
                                ),

                            ],
                            color='primary',
                            inverse=True,
                        ),
                        html.P(),
#-----------------------INDICADORES CARD--------------------------------------------------------------------------------
                        dbc.Card(
                            [
                                dbc.CardBody(
                                    [
                                        html.H5("INDICADORES", className="card-title"),
                                        html.P(
                                            """Escolha indicadores propostos por pesquisadoras(es), 
                                            ou crie os seus próprios para gerar o radar.""",
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
                                                                "Adaptação do Método Rápido de Análise de Sustentabilidade do Solo, "
                                                                "proposto por NICHOLLS e ALTIERI. Dividido em qualidade"
                                                                " do solo e saúde da collheita."
                                                            ),
                                                            dbc.Button(
                                                                "QUALIDADE DO SOLO", color="dark", id="soil",
                                                                className="mr-1"
                                                            ),
                                                            html.P(''),
                                                            dbc.Button(
                                                                "SAÚDE DA COLHEITA", color="dark", id="crop",
                                                                className="mr-1"
                                                            ),
                                                            html.P(),
                                                            dbc.Button(
                                                                "SAIBA MAIS", color="dark", id="info-button",
                                                                className="mr-1"
                                                            ),
                                                            html.P(''),
                                                            dbc.Collapse(
                                                                dbc.Card(
                                                                    dbc.CardBody(
                                                                        [
                                                                            html.P("""Esses indicadores são uma adaptação
                                                                                    dos indicadores propostos por NICHOLLS e
                                                                                    ALTIERI, 2002. Também tem como referência 
                                                                                    outra publicação com a mesma dupla e outros
                                                                                     autores, de 2004, onde adaptaram o método
                                                                                     para vinhedos. Adicionaram alguns indicadores
                                                                                     no lugar de outros, como indidência de
                                                                                     insetos "pragas" e a diversidade de seus
                                                                                     predadores. E a ideia é essa, sempre
                                                                                     adaptar ao seu agroecossistema.
                                                                                     Os artigos podem ser acessados pelos
                                                                                     links abaixo."""),
                                                                            dbc.Badge("2002",
                                                                                      href='http://www.sidalc.net/repdoc/A2039e/A2039e.pdf',
                                                                                    color = 'dark',

                                                                            ),
                                                                            html.P(''),
                                                                            dbc.Badge("2004",
                                                                                      href='https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwjxi4jhv4rsAhWqHLkGHRbeBTAQFjACegQIBxAB&url=https%3A%2F%2Fwww.researchgate.net%2Fprofile%2FBruno_Borsari%2Fpost%2FWhat_are_the_significance_of_and_strategies_for_the_maintenance_of_soil_health_in_sustainable_agriculture_How_soil_health_can_be_assessed%2Fattachment%2F5ab9096fb53d2f0bba5a6098%2FAS%253A608445061427200%25401522076015312%2Fdownload%2FNicholls_2004_Rapid_farmer_friendly_agroecological_method.pdf&usg=AOvVaw3p24teZhLMmrry2jtKoHEv',
                                                                                color='dark',

                                                                            ),
                                                                        ],
                                                                    ),
                                                                    # inverse=True,
                                                                ),
                                                                id='info-nicholls-altieri'
                                                            ),



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
                                        # INPUT 1
                                        dbc.Card(
                                            dbc.CardBody(
                                                [
                                                    html.P(''),
                                                    html.H2('Saúde da colheita'),
                                                    html.P(''),
                                                    dbc.Button(
                                                        "Ver manual", color="dark", id="crop-table-button",
                                                        className="mr-1"
                                                    ),
                                                    html.P(),
                                                    dbc.Collapse(
                                                        dbc.Card(
                                                            dbc.CardBody(
                                                                [
                                                                    table2
                                                                ]

                                                            ),
                                                            color='light'
                                                        ),
                                                        id='crop-table'
                                                    ),
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
                                                            html.P(''),
                                                            dbc.Button(
                                                                'ADICIONAR +1 ANÁLISE AO RADAR',
                                                                id='add2-crop',
                                                                color='success'
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            color='light'
                                        ),
                                        # INPUT 2
                                        dbc.Collapse(
                                            [
                                                dbc.Card(
                                                    dbc.CardBody(
                                                        [
                                                            html.P(''),
                                                            html.H2('Saúde da colheita (Análise 2)'),
                                                            html.P(''),
                                                            dbc.Form(
                                                                [
                                                                    html.Div(
                                                                        'Dê um nome para essa análise:'
                                                                    ),
                                                                    dbc.Input(
                                                                        id='name-crop2',
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
                                                                        id='aparencia2',
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
                                                                        id='crescimento2',
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
                                                                        id='resistencia2',
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
                                                                        id='incidencia2',
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
                                                                        id='competicao2',
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
                                                                        id='rendimento2',
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
                                                                        id='genetica2',
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
                                                                        id='vegetal2',
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
                                                                        id='circundante2',
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
                                                                        id='manejo2',
                                                                        placeholder='de 1 à 10',
                                                                        type='number',
                                                                        max=10,
                                                                        min=1
                                                                    ),
                                                                    html.P(''),
                                                                    dbc.Button(
                                                                        'ADICIONAR +1 ANÁLISE AO RADAR',
                                                                        id='add3-crop',
                                                                        color='success'
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    color='light',
                                                ),
                                            ],
                                            id='crop-2',
                                        ),
                                        # INPUT 3
                                        dbc.Collapse(
                                            [
                                                dbc.Card(
                                                    dbc.CardBody(
                                                        [
                                                            html.P(''),
                                                            html.H2('Saúde da colheita (Análise 3)'),
                                                            html.P(''),
                                                            dbc.Form(
                                                                [
                                                                    html.Div(
                                                                        'Dê um nome para essa análise:'
                                                                    ),
                                                                    dbc.Input(
                                                                        id='name-crop3',
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
                                                                        id='aparencia3',
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
                                                                        id='crescimento3',
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
                                                                        id='resistencia3',
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
                                                                        id='incidencia3',
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
                                                                        id='competicao3',
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
                                                                        id='rendimento3',
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
                                                                        id='genetica3',
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
                                                                        id='vegetal3',
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
                                                                        id='circundante3',
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
                                                                        id='manejo3',
                                                                        placeholder='de 1 à 10',
                                                                        type='number',
                                                                        max=10,
                                                                        min=1
                                                                    ),
                                                                    html.P(''),
                                                                    dbc.Button(
                                                                        'ADICIONAR +1 ANÁLISE AO RADAR',
                                                                        id='add4-crop',
                                                                        color='success'
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    color='light',
                                                ),
                                            ],
                                            id='crop-3',
                                        ),
                                        # INPUT 4
                                        dbc.Collapse(
                                            [
                                                dbc.Card(
                                                    dbc.CardBody(
                                                        [
                                                            html.P(''),
                                                            html.H2('Saúde da colheita (Análise 4)'),
                                                            html.P(''),
                                                            dbc.Form(
                                                                [
                                                                    html.Div(
                                                                        'Dê um nome para essa análise:'
                                                                    ),
                                                                    dbc.Input(
                                                                        id='name-crop4',
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
                                                                        id='aparencia4',
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
                                                                        id='crescimento4',
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
                                                                        id='resistencia4',
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
                                                                        id='incidencia4',
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
                                                                        id='competicao4',
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
                                                                        id='rendimento4',
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
                                                                        id='genetica4',
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
                                                                        id='vegetal4',
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
                                                                        id='circundante4',
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
                                                                        id='manejo4',
                                                                        placeholder='de 1 à 10',
                                                                        type='number',
                                                                        max=10,
                                                                        min=1
                                                                    ),
                                                                    html.P(''),
                                                                    dbc.Button(
                                                                        'ADICIONAR +1 ANÁLISE AO RADAR',
                                                                        id='add5-crop',
                                                                        color='success'
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    color='light',
                                                ),
                                            ],
                                            id='crop-4',
                                        ),
                                        # INPUT 5
                                        dbc.Collapse(
                                            [
                                                dbc.Card(
                                                    dbc.CardBody(
                                                        [
                                                            html.P(''),
                                                            html.H2('Saúde da colheita (Análise 5)'),
                                                            html.P(''),
                                                            dbc.Form(
                                                                [
                                                                    html.Div(
                                                                        'Dê um nome para essa análise:'
                                                                    ),
                                                                    dbc.Input(
                                                                        id='name-crop5',
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
                                                                        id='aparencia5',
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
                                                                        id='crescimento5',
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
                                                                        id='resistencia5',
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
                                                                        id='incidencia5',
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
                                                                        id='competicao5',
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
                                                                        id='rendimento5',
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
                                                                        id='genetica5',
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
                                                                        id='vegetal5',
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
                                                                        id='circundante5',
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
                                                                        id='manejo5',
                                                                        placeholder='de 1 à 10',
                                                                        type='number',
                                                                        max=10,
                                                                        min=1
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    color='light',
                                                ),
                                            ],
                                            id='crop-5',
                                        ),
                                        dbc.Button(
                                            'GERAR RADAR',
                                            id='show-crop-radar',
                                            color='success',
                                            block=True
                                        ),
                                        dbc.Card(
                                            dbc.CardBody(
                                                [
                                                    dcc.Graph(
                                                        id='figure-crop'
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    id='nichols-altieri-crop'
                                ),
                                # QUALIDADE DO SOLO
                                dbc.Collapse(
                                    [   # INPUT DA 1ª ANÁLISE DE QUALIDADE DO SOLO
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
                                                                id='1soil0',
                                                                type='text',
                                                                placeholder='Ex: Reforma Agrária já!'
                                                            ),
                                                            html.P(''
                                                                   ),
                                                            html.Div(indicadores[0]
                                                                     ),
                                                            dbc.Input(
                                                                id='1soil1',
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
                                                                id='1soil2',
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
                                                                id='1soil3',
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
                                                                id='1soil4',
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
                                                                id='1soil5',
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
                                                                id='1soil6',
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
                                                                id='1soil7',
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
                                                                id='1soil8',
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
                                                                id='1soil9',
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
                                                                id='1soil10',
                                                                placeholder='de 1 à 10',
                                                                type='number',
                                                                max=10,
                                                                min=1
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
                                                                        id='2soil0',
                                                                        type='text',
                                                                        placeholder='Ex: Sem Feminismo não há agroecologia!!'
                                                                    ),
                                                                    html.P(''
                                                                           ),
                                                                    html.Div(indicadores[0]
                                                                             ),
                                                                    dbc.Input(
                                                                        id='2soil1',
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
                                                                        id='2soil2',
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
                                                                        id='2soil3',
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
                                                                        id='2soil4',
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
                                                                        id='2soil5',
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
                                                                        id='2soil6',
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
                                                                        id='2soil7',
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
                                                                        id='2soil8',
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
                                                                        id='2soil9',
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
                                                                        id='2soil10',
                                                                        placeholder='de 1 à 10',
                                                                        type='number',
                                                                        max=10,
                                                                        min=1
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
                                        # INPUT DA 3ª ANÁLISE DE QUALIDADE DO SOLO
                                        dbc.Collapse(
                                            [
                                                dbc.Card(
                                                    dbc.CardBody(
                                                        [
                                                            html.P(''),
                                                            html.H2('Qualidade do solo (Análise 3)'),
                                                            html.P(''),
                                                            dbc.Form(
                                                                [
                                                                    html.Div(
                                                                        'Dê um nome para a análise:'
                                                                    ),
                                                                    dbc.Input(
                                                                        id='3soil0',
                                                                        type='text',
                                                                        placeholder='Ex: Sem Feminismo não há agroecologia!!'
                                                                    ),
                                                                    html.P(''
                                                                           ),
                                                                    html.Div(indicadores[0]
                                                                             ),
                                                                    dbc.Input(
                                                                        id='3soil1',
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
                                                                        id='3soil2',
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
                                                                        id='3soil3',
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
                                                                        id='3soil4',
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
                                                                        id='3soil5',
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
                                                                        id='3soil6',
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
                                                                        id='3soil7',
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
                                                                        id='3soil8',
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
                                                                        id='3soil9',
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
                                                                        id='3soil10',
                                                                        placeholder='de 1 à 10',
                                                                        type='number',
                                                                        max=10,
                                                                        min=1
                                                                    ),
                                                                    html.P(''),
                                                                    dbc.Button(
                                                                        'ADICIONAR +1 ANÁLISE AO RADAR',
                                                                        id='add4-soil',
                                                                        color='success'
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    color='light',
                                                    inverse=False,
                                                ),
                                            ],
                                            id='soil-3'
                                        ),
                                        # INPUT DA 4ª ANÁLISE DE QUALIDADE DO SOLO
                                        dbc.Collapse(
                                            [
                                                dbc.Card(
                                                    dbc.CardBody(
                                                        [
                                                            html.P(''),
                                                            html.H2('Qualidade do solo (Análise 4)'),
                                                            html.P(''),
                                                            dbc.Form(
                                                                [
                                                                    html.Div(
                                                                        'Dê um nome para a análise:'
                                                                    ),
                                                                    dbc.Input(
                                                                        id='4soil0',
                                                                        type='text',
                                                                        placeholder='Ex: Sem Feminismo não há agroecologia!!'
                                                                    ),
                                                                    html.P(''
                                                                           ),
                                                                    html.Div(indicadores[0]
                                                                             ),
                                                                    dbc.Input(
                                                                        id='4soil1',
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
                                                                        id='4soil2',
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
                                                                        id='4soil3',
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
                                                                        id='4soil4',
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
                                                                        id='4soil5',
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
                                                                        id='4soil6',
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
                                                                        id='4soil7',
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
                                                                        id='4soil8',
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
                                                                        id='4soil9',
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
                                                                        id='4soil10',
                                                                        placeholder='de 1 à 10',
                                                                        type='number',
                                                                        max=10,
                                                                        min=1
                                                                    ),
                                                                    html.P(''),
                                                                    dbc.Button(
                                                                        'ADICIONAR +1 ANÁLISE AO RADAR',
                                                                        id='add5-soil',
                                                                        color='success'
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    color='light',
                                                    inverse=False,
                                                ),
                                            ],
                                            id='soil-4'
                                        ),
                                        # INPUT DA 5ª ANÁLISE DE QUALIDADE DO SOLO
                                        dbc.Collapse(
                                            [
                                                dbc.Card(
                                                    dbc.CardBody(
                                                        [
                                                            html.P(''),
                                                            html.H2('Qualidade do solo (Análise 5)'),
                                                            html.P(''),
                                                            dbc.Form(
                                                                [
                                                                    html.Div(
                                                                        'Dê um nome para a análise:'
                                                                    ),
                                                                    dbc.Input(
                                                                        id='5soil0',
                                                                        type='text',
                                                                        placeholder='Ex: Sem Feminismo não há agroecologia!!'
                                                                    ),
                                                                    html.P(''
                                                                           ),
                                                                    html.Div(indicadores[0]
                                                                             ),
                                                                    dbc.Input(
                                                                        id='5soil1',
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
                                                                        id='5soil2',
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
                                                                        id='5soil3',
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
                                                                        id='5soil4',
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
                                                                        id='5soil5',
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
                                                                        id='5soil6',
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
                                                                        id='5soil7',
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
                                                                        id='5soil8',
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
                                                                        id='5soil9',
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
                                                                        id='5soil10',
                                                                        placeholder='de 1 à 10',
                                                                        type='number',
                                                                        max=10,
                                                                        min=1
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    color='light',
                                                    inverse=False,
                                                ),
                                            ],
                                            id='soil-5'
                                        ),
                                        dbc.Button(
                                            'GERAR RADAR',
                                            id='show-soil-radar',
                                            color='success',
                                            block=True
                                        ),
                                        dbc.Card(
                                            dbc.CardBody(
                                                [
                                                    dcc.Graph(
                                                        id='soil-figure'
                                                    ),
                                                    html.P(),
                                                    ],
                                                ),
                                        ),                                        # RADAR DE QUALIDADE DO SOLO 1                      
                                    ],
                                    id='nichols-altieri-soil'
                                ),
                            ],
                            id="methods",
                        ),
                        # CRIAR INDICADORES
                        dbc.Collapse(
                            [
                                # THETA INPUTS
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
                                # RADAR CHART INPUTS
                                # TRACE 1 INPUT
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
                                                                        dbc.Button('ADICIONAR +1 ANÁLISE AO RADAR', color='success',
                                                                                id='add-new-method2'),
                                                                    ],
                                                                ),
                                                            ]
                                            ),
                                        ),
                                            # TRACE 2 INPUT
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
                                            # TRACE 3 INPUT
                                            dbc.Collapse(
                                                [
                                                    dbc.Card(
                                                        dbc.CardBody(
                                                            [
                                                                dbc.Form(
                                                                    [
                                                                        html.P(),
                                                                        html.H3(id='method-name3'),
                                                                        html.P(),
                                                                        html.Div('Dê um nome para essa análise:'),
                                                                        dbc.Input(
                                                                            id='name_new3',
                                                                            type='text',
                                                                            placeholder='Ex: Pasto(03/03/2023)'
                                                                        ),
                                                                        html.P(''),
                                                                        html.Div(
                                                                            id='3new-1-out'
                                                                        ),
                                                                        dbc.Input(
                                                                            id='3new1',
                                                                            placeholder='de 1 à 10',
                                                                            type='number',
                                                                            max=10,
                                                                            min=1
                                                                        ),
                                                                        html.P(''
                                                                            ),
                                                                        html.Div(
                                                                            id='3new-2-out'
                                                                        ),
                                                                        dbc.Input(
                                                                            id='3new2',
                                                                            placeholder='de 1 à 10',
                                                                            type='number',
                                                                            max=10,
                                                                            min=1
                                                                        ),
                                                                        html.P(''
                                                                            ),
                                                                        html.Div(
                                                                            id='3new-3-out'
                                                                        ),
                                                                        dbc.Input(
                                                                            id='3new3',
                                                                            placeholder='de 1 à 10',
                                                                            type='number',
                                                                            max=10,
                                                                            min=1
                                                                        ),
                                                                        html.P(''
                                                                            ),
                                                                        html.Div(
                                                                            id='3new-4-out'
                                                                        ),
                                                                        dbc.Input(
                                                                            id='3new4',
                                                                            placeholder='de 1 à 10',
                                                                            type='number',
                                                                            max=10,
                                                                            min=1
                                                                        ),
                                                                        html.P(''
                                                                            ),
                                                                        html.Div(
                                                                            id='3new-5-out'
                                                                        ),
                                                                        dbc.Input(
                                                                            id='3new5',
                                                                            placeholder='de 1 à 10',
                                                                            type='number',
                                                                            max=10,
                                                                            min=1
                                                                        ),
                                                                        html.P(''
                                                                            ),
                                                                        html.Div(
                                                                            id='3new-6-out'
                                                                        ),
                                                                        dbc.Input(
                                                                            id='3new6',
                                                                            placeholder='de 1 à 10',
                                                                            type='number',
                                                                            max=10,
                                                                            min=1
                                                                        ),
                                                                        html.P(''
                                                                            ),
                                                                        html.Div(
                                                                            id='3new-7-out'
                                                                        ),
                                                                        dbc.Input(
                                                                            id='3new7',
                                                                            placeholder='de 1 à 10',
                                                                            type='number',
                                                                            max=10,
                                                                            min=1
                                                                        ),
                                                                        html.P(''
                                                                            ),
                                                                        html.Div(
                                                                            id='3new-8-out'
                                                                        ),
                                                                        dbc.Input(
                                                                            id='3new8',
                                                                            placeholder='de 1 à 10',
                                                                            type='number',
                                                                            max=10,
                                                                            min=1
                                                                        ),
                                                                        html.P(''
                                                                            ),
                                                                        html.Div(
                                                                            id='3new-9-out'
                                                                        ),
                                                                        dbc.Input(
                                                                            id='3new9',
                                                                            placeholder='de 1 à 10',
                                                                            type='number',
                                                                            max=10,
                                                                            min=1
                                                                        ),
                                                                        html.P(''
                                                                            ),
                                                                        html.Div(
                                                                            id='3new-10-out'
                                                                        ),
                                                                        dbc.Input(
                                                                            id='3new10',
                                                                            placeholder='de 1 à 10',
                                                                            type='number',
                                                                            max=10,
                                                                            min=1
                                                                        ),
                                                                        html.P(),
                                                                        dbc.Button('ADICIONAR +1 ANÁLISE AO RADAR', color='success',
                                                                                id='add-new-method4'
                                                                        ),
                                                                    ],
                                                                ),
                                                            ]
                                                        ),
                                                    ),
                                                    # RADAR 3
                                                    dbc.Collapse(
                                                        dbc.Card(
                                                            dbc.CardBody(
                                                                [
                                                                    dcc.Graph(
                                                                        id='figure3-new'),
                                                                ],
                                                            ),
                                                        ),
                                                        id='new-radar3'
                                                    ),
                                                ],
                                                id='maked3-method'
                                            ),
                                            # TRACE 4 INPUT
                                            dbc.Collapse(
                                                [
                                                    dbc.Card(
                                                        dbc.CardBody(
                                                            [
                                                                dbc.Form(
                                                                    [
                                                                        html.P(),
                                                                        html.H3(id='method-name4'),
                                                                        html.P(),
                                                                        html.Div('Dê um nome para essa análise:'),
                                                                        dbc.Input(
                                                                            id='name_new4',
                                                                            type='text',
                                                                            placeholder='Ex: Pasto(03/03/2023)'
                                                                        ),
                                                                        html.P(''),
                                                                        html.Div(
                                                                            id='4new-1-out'
                                                                        ),
                                                                        dbc.Input(
                                                                            id='4new1',
                                                                            placeholder='de 1 à 10',
                                                                            type='number',
                                                                            max=10,
                                                                            min=1
                                                                        ),
                                                                        html.P(''
                                                                            ),
                                                                        html.Div(
                                                                            id='4new-2-out'
                                                                        ),
                                                                        dbc.Input(
                                                                            id='4new2',
                                                                            placeholder='de 1 à 10',
                                                                            type='number',
                                                                            max=10,
                                                                            min=1
                                                                        ),
                                                                        html.P(''
                                                                            ),
                                                                        html.Div(
                                                                            id='4new-3-out'
                                                                        ),
                                                                        dbc.Input(
                                                                            id='4new3',
                                                                            placeholder='de 1 à 10',
                                                                            type='number',
                                                                            max=10,
                                                                            min=1
                                                                        ),
                                                                        html.P(''
                                                                            ),
                                                                        html.Div(
                                                                            id='4new-4-out'
                                                                        ),
                                                                        dbc.Input(
                                                                            id='4new4',
                                                                            placeholder='de 1 à 10',
                                                                            type='number',
                                                                            max=10,
                                                                            min=1
                                                                        ),
                                                                        html.P(''
                                                                            ),
                                                                        html.Div(
                                                                            id='4new-5-out'
                                                                        ),
                                                                        dbc.Input(
                                                                            id='4new5',
                                                                            placeholder='de 1 à 10',
                                                                            type='number',
                                                                            max=10,
                                                                            min=1
                                                                        ),
                                                                        html.P(''
                                                                            ),
                                                                        html.Div(
                                                                            id='4new-6-out'
                                                                        ),
                                                                        dbc.Input(
                                                                            id='4new6',
                                                                            placeholder='de 1 à 10',
                                                                            type='number',
                                                                            max=10,
                                                                            min=1
                                                                        ),
                                                                        html.P(''
                                                                            ),
                                                                        html.Div(
                                                                            id='4new-7-out'
                                                                        ),
                                                                        dbc.Input(
                                                                            id='4new7',
                                                                            placeholder='de 1 à 10',
                                                                            type='number',
                                                                            max=10,
                                                                            min=1
                                                                        ),
                                                                        html.P(''
                                                                            ),
                                                                        html.Div(
                                                                            id='4new-8-out'
                                                                        ),
                                                                        dbc.Input(
                                                                            id='4new8',
                                                                            placeholder='de 1 à 10',
                                                                            type='number',
                                                                            max=10,
                                                                            min=1
                                                                        ),
                                                                        html.P(''
                                                                            ),
                                                                        html.Div(
                                                                            id='4new-9-out'
                                                                        ),
                                                                        dbc.Input(
                                                                            id='4new9',
                                                                            placeholder='de 1 à 10',
                                                                            type='number',
                                                                            max=10,
                                                                            min=1
                                                                        ),
                                                                        html.P(''
                                                                            ),
                                                                        html.Div(
                                                                            id='4new-10-out'
                                                                        ),
                                                                        dbc.Input(
                                                                            id='4new10',
                                                                            placeholder='de 1 à 10',
                                                                            type='number',
                                                                            max=10,
                                                                            min=1
                                                                        ),
                                                                        html.P(),
                                                                        dbc.Button('ADICIONAR +1 ANÁLISE AO RADAR', color='success',
                                                                                id='add-new-method5'
                                                                        ),
                                                                    ],
                                                                ),
                                                            ]
                                                        ),
                                                    ),
                                                ],
                                                id='maked4-method'
                                            ),
                                            # TRACE 5 INPUT
                                            dbc.Collapse(
                                                [
                                                    dbc.Card(
                                                        dbc.CardBody(
                                                            [
                                                                dbc.Form(
                                                                    [
                                                                        html.P(),
                                                                        html.H3(id='method-name5'),
                                                                        html.P(),
                                                                        html.Div('Dê um nome para essa análise:'),
                                                                        dbc.Input(
                                                                            id='name_new5',
                                                                            type='text',
                                                                            placeholder='Ex: Pasto(03/03/2023)'
                                                                        ),
                                                                        html.P(''),
                                                                        html.Div(
                                                                            id='5new-1-out'
                                                                        ),
                                                                        dbc.Input(
                                                                            id='5new1',
                                                                            placeholder='de 1 à 10',
                                                                            type='number',
                                                                            max=10,
                                                                            min=1
                                                                        ),
                                                                        html.P(''
                                                                            ),
                                                                        html.Div(
                                                                            id='5new-2-out'
                                                                        ),
                                                                        dbc.Input(
                                                                            id='5new2',
                                                                            placeholder='de 1 à 10',
                                                                            type='number',
                                                                            max=10,
                                                                            min=1
                                                                        ),
                                                                        html.P(''
                                                                            ),
                                                                        html.Div(
                                                                            id='5new-3-out'
                                                                        ),
                                                                        dbc.Input(
                                                                            id='5new3',
                                                                            placeholder='de 1 à 10',
                                                                            type='number',
                                                                            max=10,
                                                                            min=1
                                                                        ),
                                                                        html.P(''
                                                                            ),
                                                                        html.Div(
                                                                            id='5new-4-out'
                                                                        ),
                                                                        dbc.Input(
                                                                            id='5new4',
                                                                            placeholder='de 1 à 10',
                                                                            type='number',
                                                                            max=10,
                                                                            min=1
                                                                        ),
                                                                        html.P(''
                                                                            ),
                                                                        html.Div(
                                                                            id='5new-5-out'
                                                                        ),
                                                                        dbc.Input(
                                                                            id='5new5',
                                                                            placeholder='de 1 à 10',
                                                                            type='number',
                                                                            max=10,
                                                                            min=1
                                                                        ),
                                                                        html.P(''
                                                                            ),
                                                                        html.Div(
                                                                            id='5new-6-out'
                                                                        ),
                                                                        dbc.Input(
                                                                            id='5new6',
                                                                            placeholder='de 1 à 10',
                                                                            type='number',
                                                                            max=10,
                                                                            min=1
                                                                        ),
                                                                        html.P(''
                                                                            ),
                                                                        html.Div(
                                                                            id='5new-7-out'
                                                                        ),
                                                                        dbc.Input(
                                                                            id='5new7',
                                                                            placeholder='de 1 à 10',
                                                                            type='number',
                                                                            max=10,
                                                                            min=1
                                                                        ),
                                                                        html.P(''
                                                                            ),
                                                                        html.Div(
                                                                            id='5new-8-out'
                                                                        ),
                                                                        dbc.Input(
                                                                            id='5new8',
                                                                            placeholder='de 1 à 10',
                                                                            type='number',
                                                                            max=10,
                                                                            min=1
                                                                        ),
                                                                        html.P(''
                                                                            ),
                                                                        html.Div(
                                                                            id='5new-9-out'
                                                                        ),
                                                                        dbc.Input(
                                                                            id='5new9',
                                                                            placeholder='de 1 à 10',
                                                                            type='number',
                                                                            max=10,
                                                                            min=1
                                                                        ),
                                                                        html.P(''
                                                                            ),
                                                                        html.Div(
                                                                            id='5new-10-out'
                                                                        ),
                                                                        dbc.Input(
                                                                            id='5new10',
                                                                            placeholder='de 1 à 10',
                                                                            type='number',
                                                                            max=10,
                                                                            min=1
                                                                        ),
                                                                    ],
                                                                ),
                                                            ]
                                                        ),
                                                    ),
                                                ],
                                                id='maked5-method'
                                            ),
                                            html.P(),
                                            dbc.Button('GERAR RADAR', color='success', block=True,
                                                    id='show-new-radar'
                                            ),
                                            # RADAR CHART OUTPUT
                                            dbc.Card(
                                                dbc.CardBody(
                                                    [
                                                    dcc.Graph(
                                                        id='custom-figure', figure={}
                                                        ),
                                                    ],
                                                ),
                                            ), 
                                    ],
                                id='maked-method'
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
#--------------------------------------------------------------------COLLAPSE CALLBACKS---------------------------------

#----------------------------CUSTOM METHOD------------------------------------------------------------------------------


# INPUT 1
@app.callback(
    Output('maked-method', 'is_open'),
    [Input("save-new-method", "n_clicks")],
    [State("maked-method", "is_open")],
    prevent_initial_call=True
)
def open_maked_method(n, is_open):
    if n:
        return not is_open
    return is_open

# INPUT 2
@app.callback(
    Output('maked2-method', 'is_open'),
    [Input("add-new-method2", "n_clicks")],
    [State("maked2-method", "is_open")],
    prevent_initial_call=True
)
def open_maked_method(n, is_open):
    if n:
        return not is_open
    return is_open

# INPUT 3
@app.callback(
    Output('maked3-method', 'is_open'),
    [Input("add-new-method3", "n_clicks")],
    [State("maked3-method", "is_open")],
    prevent_initial_call=True
)
def open_maked_method(n, is_open):
    if n:
        return not is_open
    return is_open

# INPUT 4
@app.callback(
    Output('maked4-method', 'is_open'),
    [Input("add-new-method4", "n_clicks")],
    [State("maked4-method", "is_open")],
    prevent_initial_call=True
)
def open_maked_method(n, is_open):
    if n:
        return not is_open
    return is_open

# INPUT 5
@app.callback(
    Output('maked5-method', 'is_open'),
    [Input("add-new-method5", "n_clicks")],
    [State("maked5-method", "is_open")],
    prevent_initial_call=True
)
def open_maked_method(n, is_open):
    if n:
        return not is_open
    return is_open

# CUSTOM RADAR 
@app.callback(
    Output('custom-figure', 'figure'),
    Input("show-new-radar", "n_clicks"),
    [State('new-method-name', 'value'),
     State('name_new', 'value'),
     State('new1', 'value'),
     State('new2', 'value'),
     State('new3', 'value'),
     State('new4', 'value'),
     State('new5', 'value'),
     State('new6', 'value'),
     State('new7', 'value'),
     State('new8', 'value'),
     State('new9', 'value'),
     State('new10', 'value'),
     State('name_new2', 'value'),
     State('2new1', 'value'),
     State('2new2', 'value'),
     State('2new3', 'value'),
     State('2new4', 'value'),
     State('2new5', 'value'),
     State('2new6', 'value'),
     State('2new7', 'value'),
     State('2new8', 'value'),
     State('2new9', 'value'),
     State('2new10', 'value'),
     State('name_new3', 'value'),
     State('3new1', 'value'),
     State('3new2', 'value'),
     State('3new3', 'value'),
     State('3new4', 'value'),
     State('3new5', 'value'),
     State('3new6', 'value'),
     State('3new7', 'value'),
     State('3new8', 'value'),
     State('3new9', 'value'),
     State('3new10', 'value'),
     State('name_new4', 'value'),
     State('4new1', 'value'),
     State('4new2', 'value'),
     State('4new3', 'value'),
     State('4new4', 'value'),
     State('4new5', 'value'),
     State('4new6', 'value'),
     State('4new7', 'value'),
     State('4new8', 'value'),
     State('4new9', 'value'),
     State('4new10', 'value'),
     State('name_new5', 'value'),
     State('5new1', 'value'),
     State('5new2', 'value'),
     State('5new3', 'value'),
     State('5new4', 'value'),
     State('5new5', 'value'),
     State('5new6', 'value'),
     State('5new7', 'value'),
     State('5new8', 'value'),
     State('5new9', 'value'),
     State('5new10', 'value'),

     State('cria1', 'value'),
     State('cria2', 'value'),
     State('cria3', 'value'),
     State('cria4', 'value'),
     State('cria5', 'value'),
     State('cria6', 'value'),
     State('cria7', 'value'),
     State('cria8', 'value'),
     State('cria9', 'value'),
     State('cria10', 'value'),
     ],
    prevent_initial_call=True
)
def custom_radar_graph (n, title, name1, ind11, ind21, ind31, ind41, ind51, ind61, ind71, ind81, ind91, ind101,
                       name2, ind12, ind22, ind32, ind42, ind52, ind62, ind72, ind82, ind92, ind102,
                       name3, ind13, ind23, ind33, ind43, ind53, ind63, ind73, ind83, ind93, ind103,
                       name4, ind14, ind24, ind34, ind44, ind54, ind64, ind74, ind84, ind94, ind104,
                       name5, ind15, ind25, ind35, ind45, ind55, ind65, ind75, ind85, ind95, ind105,
                       out1, out2, out3, out4, out5, out6, out7, out8, out9, out10):

    theta = [out1, out2, out3, out4, out5, out6, out7, out8, out9, out10]
    trace1 = [ind11, ind21, ind31, ind41, ind51, ind61, ind71, ind81, ind91, ind101]
    trace2 = [ind12, ind22, ind32, ind42, ind52, ind62, ind72, ind82, ind92, ind102]
    trace3 = [ind13, ind23, ind33, ind43, ind53, ind63, ind73, ind83, ind93, ind103]
    trace4 = [ind14, ind24, ind34, ind44, ind54, ind64, ind74, ind84, ind94, ind104]
    trace5 = [ind15, ind25, ind35, ind45, ind55, ind65, ind75, ind85, ind95, ind105]
   

    if name2 == None and name3 == None and name4 == None and name5 == None:
        fig = radar_chart(
                    name1 = name1, 
                    r1 = trace1,
                    theta = theta,
                    title=title
                ) 
    elif name3 == None  and name4 == None and name5 == None: 
        fig = radar_chart(
                    name1 = name1, 
                    name2 = name2, 
                    r1 = trace1,
                    r2 = trace2,
                    theta = theta,
                    title=title
                ) 
    elif name4 == None and name5 == None:
        fig = radar_chart(
                    name1 = name1, 
                    name2 = name2, 
                    name3 = name3,
                    r1 = trace1,
                    r2 = trace2,
                    r3 = trace3,
                    theta = theta,
                    title=title
                )   

    elif name5 == None:
        fig = radar_chart(
                    name1 = name1, 
                    name2 = name2, 
                    name3 = name3,
                    name4 = name4,
                    r1 = trace1,
                    r2 = trace2,
                    r3 = trace3,
                    r4 = trace4,
                    theta = theta,
                    title=title
                )
    else:
        fig = radar_chart(
                    name1 = name1, 
                    name2 = name2, 
                    name3 = name3,
                    name4 = name4,
                    name5 = name5,
                    r1 = trace1,
                    r2 = trace2,
                    r3 = trace3,
                    r4 = trace4,
                    r5 = trace5,
                    theta = theta,
                    title=title
                )

    return fig


#-----------------------------------------------METHODS-----------------------------------------------------------------
# SHOW METHODS
############################################################################

@app.callback(
    [
        Output('methods', 'is_open'),
        Output('new-method', 'is_open'),
    ],
    [
        Input("methods-button", "n_clicks"),
        Input("new-method-button", "n_clicks"),
    ],
    [
        State('methods', 'is_open'),
        State('new-method', 'is_open'),
    ],
)
def initial_menu(n1, n2, is_open1, is_open2):
    """Controle da abertura/ fechamento dos collapses do menu inicial"""
    ctx = dash.callback_context

    if not ctx.triggered:
        return False, False
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if button_id == "methods-button" and n1:
        return not is_open1, False

    elif button_id == "new-method-button" and n2:
        return False, not is_open2
    return False, False

@app.callback(
    [
        Output("nichols-altieri-soil", "is_open"),
        Output("nichols-altieri-crop", "is_open"),
        Output("info-nicholls-altieri", "is_open"),
    ],
    [
        Input("soil", 'n_clicks'),
        Input("crop", 'n_clicks'),
        Input("info-button", 'n_clicks'),
    ],
    [
        State("nichols-altieri-soil", "is_open"),
        State("nichols-altieri-crop", "is_open"),
        State("info-nicholls-altieri", "is_open"),
    ],
)
def methods_menu(n1, n2, n3, is_open1, is_open2, is_open3):
    ctx = dash.callback_context

    if not ctx.triggered:
        return False, False, False
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if button_id == "soil" and n1:
        return not is_open1, False, False

    elif button_id == "crop" and n2:
        return False, not is_open2, False
    
    elif button_id == "info-button" and n3:
        return False, False, not is_open3

    return False, False, False

# 
#----------------------------SAÚDE DA COLHEITA--------------------------------------------------------------------------
# MANUAL
@app.callback(
    Output('crop-table', 'is_open'),
    [Input("crop-table-button", "n_clicks")],
    [State("crop-table", "is_open")],
    prevent_initial_call=True
)
def open_soil_table(n, is_open):
    if n:
        return not is_open
    return is_open

# INPUT 2
@app.callback(
    Output('crop-2', 'is_open'),
    [Input("add2-crop", "n_clicks")],
    [State("crop-2", "is_open")],
    prevent_initial_call=True
)
def open_crop(n, is_open):
    if n:
        return not is_open
    return is_open

# INPUT 3
@app.callback(
    Output('crop-3', 'is_open'),
    [Input("add3-crop", "n_clicks")],
    [State("crop-3", "is_open")],
    prevent_initial_call=True
)
def open_crop(n, is_open):
    if n:
        return not is_open
    return is_open

# INPUT 4
@app.callback(
    Output('crop-4', 'is_open'),
    [Input("add4-crop", "n_clicks")],
    [State("crop-4", "is_open")],
    prevent_initial_call=True
)
def open_crop(n, is_open):
    if n:
        return not is_open
    return is_open

# INPUT 5
@app.callback(
    Output('crop-5', 'is_open'),
    [Input("add5-crop", "n_clicks")],
    [State("crop-5", "is_open")],
    prevent_initial_call=True
)
def open_crop(n, is_open):
    if n:
        return not is_open
    return is_open

# SOIL HEALTH RADAR OUTPUT
@app.callback(
    Output('figure-crop', 'figure'),
    Input("show-crop-radar", 'n_clicks'),
    [State('name-crop', 'value'),
     State('aparencia', 'value'),
     State('crescimento', 'value'),
     State('resistencia', 'value'),
     State('incidencia', 'value'),
     State('competicao', 'value'),
     State('rendimento', 'value'),
     State('genetica', 'value'),
     State('vegetal', 'value'),
     State('circundante', 'value'),
     State('manejo', 'value'),
     State('name-crop2', 'value'),
     State('aparencia2', 'value'),
     State('crescimento2', 'value'),
     State('resistencia2', 'value'),
     State('incidencia2', 'value'),
     State('competicao2', 'value'),
     State('rendimento2', 'value'),
     State('genetica2', 'value'),
     State('vegetal2', 'value'),
     State('circundante2', 'value'),
     State('manejo2', 'value'),
     State('name-crop3', 'value'),
     State('aparencia3', 'value'),
     State('crescimento3', 'value'),
     State('resistencia3', 'value'),
     State('incidencia3', 'value'),
     State('competicao3', 'value'),
     State('rendimento3', 'value'),
     State('genetica3', 'value'),
     State('vegetal3', 'value'),
     State('circundante3', 'value'),
     State('manejo3', 'value'),
     State('name-crop4', 'value'),
     State('aparencia4', 'value'),
     State('crescimento4', 'value'),
     State('resistencia4', 'value'),
     State('incidencia4', 'value'),
     State('competicao4', 'value'),
     State('rendimento4', 'value'),
     State('genetica4', 'value'),
     State('vegetal4', 'value'),
     State('circundante4', 'value'),
     State('manejo4', 'value'),
     State('name-crop5', 'value'),
     State('aparencia5', 'value'),
     State('crescimento5', 'value'),
     State('resistencia5', 'value'),
     State('incidencia5', 'value'),
     State('competicao5', 'value'),
     State('rendimento5', 'value'),
     State('genetica5', 'value'),
     State('vegetal5', 'value'),
     State('circundante5', 'value'),
     State('manejo5', 'value'),],
     prevent_initial_call=True
)
def chart_crop_update (n, name1, ind1, ind2, ind3, ind4, ind5, ind6, ind7, ind8, ind9, ind10,
                        name2, ind12, ind22, ind32, ind42, ind52, ind62, ind72, ind82, ind92, ind102,
                        name3, ind13, ind23, ind33, ind43, ind53, ind63, ind73, ind83, ind93, ind103,
                        name4, ind14, ind24, ind34, ind44, ind54, ind64, ind74, ind84, ind94, ind104,
                        name5, ind15, ind25, ind35, ind45, ind55, ind65, ind75, ind85, ind95, ind105):

    trace1 = [ind1, ind2, ind3, ind4, ind5, ind6, ind7, ind8, ind9, ind10]
    trace2 = [ind12, ind22, ind32, ind42, ind52, ind62, ind72, ind82, ind92, ind102]
    trace3 = [ind13, ind23, ind33, ind43, ind53, ind63, ind73, ind83, ind93, ind103]
    trace4 = [ind14, ind24, ind34, ind44, ind54, ind64, ind74, ind84, ind94, ind104]
    trace5 = [ind15, ind25, ind35, ind45, ind55, ind65, ind75, ind85, ind95, ind105]
    theta = ['Aparência', 'Crescimento', 'Resistência à estresse',
             'Incidência de doenças', 'Competição com espontâneas',
             'Rendimento', 'Diversidade genética', 'Diversidade vegetal',
             'Diversidade natural circundante', 'Sistema de manejo']
    title = "Saúde da colheita"

    if name2 == None and name3 == None and name4 == None and name5 == None:
        fig = radar_chart(
                    name1 = name1, 
                    r1 = trace1,
                    theta = theta,
                    title=title
                ) 
    elif name3 == None  and name4 == None and name5 == None: 
        fig = radar_chart(
                    name1 = name1, 
                    name2 = name2, 
                    r1 = trace1,
                    r2 = trace2,
                    theta = theta,
                    title=title
                ) 
    elif name4 == None and name5 == None:
        fig = radar_chart(
                    name1 = name1, 
                    name2 = name2, 
                    name3 = name3,
                    r1 = trace1,
                    r2 = trace2,
                    r3 = trace3,
                    theta = theta,
                    title=title
                )   

    elif name5 == None:
        fig = radar_chart(
                    name1 = name1, 
                    name2 = name2, 
                    name3 = name3,
                    name4 = name4,
                    r1 = trace1,
                    r2 = trace2,
                    r3 = trace3,
                    r4 = trace4,
                    theta = theta,
                    title=title
                )
    else:
        fig = radar_chart(
                    name1 = name1, 
                    name2 = name2, 
                    name3 = name3,
                    name4 = name4,
                    name5 = name5,
                    r1 = trace1,
                    r2 = trace2,
                    r3 = trace3,
                    r4 = trace4,
                    r5 = trace5,
                    theta = theta,
                    title=title
                )

    return fig


#----------------------------QUALIDADE DO SOLO--------------------------------------------------------------------------
# MANUAL
@app.callback(
    Output('soil-table', 'is_open'),
    [Input("soil-table-button", "n_clicks")],
    [State("soil-table", "is_open")],
    prevent_initial_call=True
)
def open_soil_table(n, is_open):
    if n:
        return not is_open
    return is_open



# INPUT 2
@app.callback(
    Output('soil-2', 'is_open'),
    [Input("add2-soil", "n_clicks")],
    [State("soil-2", "is_open")],
    prevent_initial_call=True
)
def open_crop(n, is_open):
    if n:
        return not is_open
    return is_open

# INPUT 3
@app.callback(
    Output('soil-3', 'is_open'),
    [Input("add3-soil", "n_clicks")],
    [State("soil-3", "is_open")],
    prevent_initial_call=True
)
def open_crop(n, is_open):
    if n:
        return not is_open
    return is_open

# INPUT 4
@app.callback(
    Output('soil-4', 'is_open'),
    [Input("add4-soil", "n_clicks")],
    [State("soil-4", "is_open")],
    prevent_initial_call=True
)
def open_crop(n, is_open):
    if n:
        return not is_open
    return is_open

# INPUT 5
@app.callback(
    Output('soil-5', 'is_open'),
    [Input("add5-soil", "n_clicks")],
    [State("soil-5", "is_open")],
    prevent_initial_call=True
)
def open_crop(n, is_open):
    if n:
        return not is_open
    return is_open

lista_forms_soil = []    
for i in range(1, 6):
    for x in range(11):
        lista_forms_soil.append(State(f'{i}soil{x}', 'value'))

# SOIL RADAR OUTPUT
@app.callback(
    Output('soil-figure', 'figure'),
    Input("show-soil-radar", "n_clicks"),
    lista_forms_soil,
    prevent_initial_call=True
)
def add_analise(n,
        soil_name1, soil_1_1, soil_1_2, soil_1_3, soil_1_4, soil_1_5, soil_1_6,
            soil_1_7, soil_1_8, soil_1_9, soil_1_10,

        soil_name2, soil_2_1, soil_2_2, soil_2_3, soil_2_4, soil_2_5,
            soil_2_6, soil_2_7, soil_2_8, soil_2_9, soil_2_10,

        soil_name3, soil_3_1, soil_3_2, soil_3_3, soil_3_4, soil_3_5, soil_3_6, soil_3_7,
            soil_3_8, soil_3_9, soil_3_10,
                        
        soil_name4, soil_4_1, soil_4_2, soil_4_3, soil_4_4, soil_4_5, soil_4_6, soil_4_7,
            soil_4_8, soil_4_9, soil_4_10,

        soil_name5, soil_5_1, soil_5_2, soil_5_3, soil_5_4, soil_5_5, soil_5_6, soil_5_7,
                soil_5_8, soil_5_9, soil_5_10
):

    trace1 = [soil_1_1, soil_1_2, soil_1_3, soil_1_4, soil_1_5, soil_1_6, soil_1_7, 
                soil_1_8, soil_1_9, soil_1_10]
    trace2 = [soil_2_1, soil_2_2, soil_2_3, soil_2_4, soil_2_5, soil_2_6, soil_2_7, 
                soil_2_8, soil_2_9, soil_2_10]
    trace3 = [soil_3_1, soil_3_2, soil_3_3, soil_3_4, soil_3_5, soil_3_6, soil_3_7,
                soil_3_8, soil_3_9, soil_3_10]
    trace4 = [soil_4_1, soil_4_2, soil_4_3, soil_4_4, soil_4_5, soil_4_6, soil_4_7,
                soil_4_8, soil_4_9, soil_4_10]
    trace5 = [soil_5_1, soil_5_2, soil_5_3, soil_5_4, soil_5_5, soil_5_6, soil_5_7,
                soil_5_8, soil_5_9, soil_5_10]

    theta = ["Estrutura", "Compactação e infiltração", "Produndidade do solo",
              "Estado dos resíduos", "Cor, cheiro e matéria orgânica", "Retenção da umidade",
               "Desenvolvimento de raízes", "Cobertura do solo", "Erosão", "Atividade biológica"]
    title = "Qualidade do solo"

    if soil_name2 == None and soil_name3 == None and soil_name4 == None and soil_name5 == None:
        fig = radar_chart(
                    name1 = soil_name1, 
                    r1 = trace1,
                    theta = theta,
                    title=title
                ) 
    elif soil_name3 == None  and soil_name4 == None and soil_name5 == None: 
        fig = radar_chart(
                    name1 = soil_name1, 
                    name2 = soil_name2, 
                    r1 = trace1,
                    r2 = trace2,
                    theta = theta,
                    title=title
                ) 
    elif soil_name4 == None and soil_name5 == None:
        fig = radar_chart(
                    name1 = soil_name1, 
                    name2 = soil_name2, 
                    name3 = soil_name3,
                    r1 = trace1,
                    r2 = trace2,
                    r3 = trace3,
                    theta = theta,
                    title=title
                )   

    elif soil_name5 == None:
        fig = radar_chart(
                    name1 = soil_name1, 
                    name2 = soil_name2, 
                    name3 = soil_name3,
                    name4 = soil_name4,
                    r1 = trace1,
                    r2 = trace2,
                    r3 = trace3,
                    r4 = trace4,
                    theta = theta,
                    title=title
                )
    else:
        fig = radar_chart(
                    name1 = soil_name1, 
                    name2 = soil_name2, 
                    name3 = soil_name3,
                    name4 = soil_name4,
                    name5 = soil_name5,
                    r1 = trace1,
                    r2 = trace2,
                    r3 = trace3,
                    r4 = trace4,
                    r5 = trace5,
                    theta = theta,
                    title=title
                )

    return fig


#--------------------CUSTOM METHOD UPDATE-------------------------------------------------------------------------------
#  TODO: tirar os prevent call dos formularios de criação de indicadores 
@app.callback(
    [Output('method-name', 'children'),
     Output('method-name2', 'children'),
     Output('method-name3', 'children'),
     Output('method-name4', 'children'),
     Output('method-name5', 'children')],
    [Input('new-method-name', 'value')],
    prevent_initial_call=True
)
def update_new_output(input_value):
    return f'{input_value} (Análise 1)', f'{input_value} (Análise 2)', f'{input_value} (Análise 3)', f'{input_value} (Análise 4)', f'{input_value} (Análise 5)'

@app.callback(
    [Output('new-1-out', 'children'),
    Output('2new-1-out', 'children'),
     Output('3new-1-out', 'children'),
     Output('4new-1-out', 'children'),
     Output('5new-1-out', 'children')],
    [Input('cria1', 'value')],
    prevent_initial_call=True
)
def update_new_output(input_value):
    return f'{input_value}: ', f'{input_value}: ', f'{input_value}: ', f'{input_value}: ', f'{input_value}: '

@app.callback(
    [Output('new-2-out', 'children'),
     Output('2new-2-out', 'children'),
     Output('3new-2-out', 'children'),
     Output('4new-2-out', 'children'),
     Output('5new-2-out', 'children')],
    [Input('cria2', 'value')],
    prevent_initial_call=True
)
def update_new_output(input_value):
    return f'{input_value}: ', f'{input_value}: ', f'{input_value}: ', f'{input_value}: ', f'{input_value}: '

@app.callback(
    [Output('new-3-out', 'children'),
     Output('2new-3-out', 'children'),
     Output('3new-3-out', 'children'),
     Output('4new-3-out', 'children'),
     Output('5new-3-out', 'children'),],
    [Input('cria3', 'value')],
    prevent_initial_call=True
)
def update_new_output(input_value):
    return f'{input_value}: ', f'{input_value}: ', f'{input_value}: ', f'{input_value}: ', f'{input_value}: '

@app.callback(
    [Output('new-4-out', 'children'),
     Output('2new-4-out', 'children'),
     Output('3new-4-out', 'children'),
     Output('4new-4-out', 'children'),
     Output('5new-4-out', 'children'),],
    [Input('cria4', 'value')],
    prevent_initial_call=True
)
def update_new_output(input_value):
    return f'{input_value}: ', f'{input_value}: ', f'{input_value}: ', f'{input_value}: ', f'{input_value}: '

@app.callback(
    [Output('new-5-out', 'children'),
     Output('2new-5-out', 'children'),
     Output('3new-5-out', 'children'),
     Output('4new-5-out', 'children'),
     Output('5new-5-out', 'children'),],
    [Input('cria5', 'value')],
    prevent_initial_call=True
)
def update_new_output(input_value):
    return f'{input_value}: ', f'{input_value}: ', f'{input_value}: ', f'{input_value}: ', f'{input_value}: '

@app.callback(
    [Output('new-6-out', 'children'),
     Output('2new-6-out', 'children'),
     Output('3new-6-out', 'children'),
     Output('4new-6-out', 'children'),
     Output('5new-6-out', 'children'),],
    [Input('cria6', 'value')],
    prevent_initial_call=True
)
def update_new_output(input_value):
    return f'{input_value}: ', f'{input_value}: ', f'{input_value}: ', f'{input_value}: ', f'{input_value}: '

@app.callback(
    [Output('new-7-out', 'children'),
     Output('2new-7-out', 'children'),
     Output('3new-7-out', 'children'),
     Output('4new-7-out', 'children'),
     Output('5new-7-out', 'children'),],
    [Input('cria7', 'value')],
    prevent_initial_call=True
)
def update_new_output(input_value):
    return f'{input_value}: ', f'{input_value}: ', f'{input_value}: ', f'{input_value}: ', f'{input_value}: '

@app.callback(
    [Output('new-8-out', 'children'),
     Output('2new-8-out', 'children'),
     Output('3new-8-out', 'children'),
     Output('4new-8-out', 'children'),
     Output('5new-8-out', 'children'),],
    [Input('cria8', 'value')],
    prevent_initial_call=True
)
def update_new_output(input_value):
    return f'{input_value}: ', f'{input_value}: ', f'{input_value}: ', f'{input_value}: ', f'{input_value}: '

@app.callback(
    [Output('new-9-out', 'children'),
     Output('2new-9-out', 'children'),
     Output('3new-9-out', 'children'),
     Output('4new-9-out', 'children'),
     Output('5new-9-out', 'children'),],
    [Input('cria9', 'value')],
    prevent_initial_call=True
)
def update_new_output(input_value):
    return f'{input_value}: ', f'{input_value}: ', f'{input_value}: ', f'{input_value}: ', f'{input_value}: '

@app.callback(
    [Output('new-10-out', 'children'),
    Output('2new-10-out', 'children'),
     Output('3new-10-out', 'children'),
     Output('4new-10-out', 'children'),
     Output('5new-10-out', 'children'),],
    [Input('cria10', 'value')],
    prevent_initial_call=True
)
def update_new_output(input_value):
    return f'{input_value}: ', f'{input_value}: ', f'{input_value}: ', f'{input_value}: ', f'{input_value}: '

#-----------------------------------------------------------------------------------APP RUN-----------------------------
if __name__ == '__main__':
    app.run_server(debug=False)
    # app.run_server(port=8050,host='0.0.0.0')