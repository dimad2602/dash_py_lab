from dash import html
import dash_bootstrap_components as dbc


def get_tab3_content():
    table_header = [
        html.Thead(html.Tr([html.Th("Field Name"),
                            html.Th("Detailds")]))
    ]

    expl = {
        'KOI': 'Object of Interest number',
        'A': 'Semi-major axis (AU)',
        'RPLANET': 'Planetary radius (Earth radii)',
        'RSTAR': 'Stellar radius (Sol radii)',
        'TSTAR': 'Effective temperature of host star as reported in KIC (k)',
        'KMAG': '	Kepler magnitude (kmag)',
        'TPLANET': 'Equilibrium temperature of planet, per orucki et al. (k)',
        'T0	Time ': 'of transit center (BJD-2454900)',
        'UT0': 'Uncertainty in time of transit center (+-jd)',
        'UT0': 'Uncertainty in time of transit center (+-jd)',
        'PER': 'Period (days)',
        'UPER': 'Uncertainty in period (+-days)',
        'DEC': 'Declination (@J200)',
        'RA	Right': 'ascension (@J200)',
        'MSTAR': 'Derived stellar mass (msol)'
    }

    tbl_rows = []
    for i in expl:
        tbl_rows.append(html.Tr([html.Td(i), html.Td(expl[i])]))

    table_body = [html.Tbody(tbl_rows)]

    table = dbc.Table(table_header + table_body, bordered=True)

    tab3_content = [
        dbc.Row(html.A('Data are sourced from Kepler API via asterank.com',
                       href='https://www.asterank.com/kepler'),
                style={'margin-top': 20}),
        dbc.Row(html.Div(children=table), style={'margin-top': 20})
    ]
    return tab3_content
