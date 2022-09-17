"""Dashboard app layout."""

from dash import dcc, html

from features.ui.layout.header.index import header
from features.ui.layout.leftbar.index import leftbar
from features.ui.layout.topbar.index import topbar


def layout():
    """Dashboard app layout."""
    content = html.Div([html.H1("Content")], id="page-content")
    return html.Div(
        [
            dcc.Location(id="url"),
            leftbar(),
            html.Div(
                [header(), topbar(), content],
                className="grid col-span-10 bg-sky-500/100",
            ),
        ],
        className="grid grid-cols-12",
    )
