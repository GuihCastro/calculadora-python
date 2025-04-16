from variables import PRIMARY, PRIMARY_DARK, PRIMARY_DARKER, PRIMARY_LIGHT, WHITE, SMALL


qss = f"""
    QLineEdit {{
        color: {WHITE};
    }}
    QPushButton {{
        font-size: {SMALL}px;
        border: 1px solid {WHITE};
        border-radius: 6px;
        background: transparent;
    }}
    QPushButton:hover {{
        color: {PRIMARY_LIGHT};
        border: 1px solid {PRIMARY};
    }}
    QPushButton:pressed {{
        color: {WHITE};
        border: 1px solid {PRIMARY_DARK};
    }}
    QPushButton[cssClass="specialButton"] {{
        color: {WHITE};
        background: {PRIMARY};
        border: none;
        border-radius: 6px;
    }}
    QPushButton[cssClass="specialButton"]:hover {{
        color: {WHITE};
        background: {PRIMARY_DARK};
    }}
    QPushButton[cssClass="specialButton"]:pressed {{
        color: {WHITE};
        background: {PRIMARY_DARKER};
    }}
"""
