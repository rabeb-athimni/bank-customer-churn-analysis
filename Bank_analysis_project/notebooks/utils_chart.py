import plotly.express as px


COLORS = [
    "#B0D5D5",
    "#BB648D",
    "#1BAAA0",
    "#FF9F7A",
    "#DB6A8F",
    "#5784BA"
]


# PIE CHART
def create_pie_chart(data, names_col, values_col, title):
    
    fig = px.pie(
        data,
        names=names_col,
        values=values_col,
        title=title,
        hole=0.4,
        color_discrete_sequence=COLORS
    )

    return fig


# BAR CHART
def create_bar_chart(data, x_col, y_col, title, color_col=None):

    fig = px.bar(
        data,
        x=x_col,
        y=y_col,
        color=color_col,
        title=title,
        color_discrete_sequence=COLORS
    )

    return fig


# HISTOGRAM
def create_histogram(data, x_col, title):

    fig = px.histogram(
        data,
        x=x_col,
        title=title,
        color_discrete_sequence=COLORS
    )

    return fig


# BOX PLOT
def create_box_plot(data, x_col, y_col, title, color_col=None):

    fig = px.box(
        data,
        x=x_col,
        y=y_col,
        color=color_col,
        title=title,
        color_discrete_sequence=COLORS
    )

    return fig


# SCATTER PLOT
def create_scatter_plot(data, x_col, y_col, title, color_col=None):

    fig = px.scatter(
        data,
        x=x_col,
        y=y_col,
        color=color_col,
        title=title,
        color_discrete_sequence=COLORS
    )

    return fig
def create_heatmap(data, title):

    fig = px.imshow(
        data,
        text_auto=True,
        aspect="auto",
        color_continuous_scale="RdBu_r",
        title=title
    )

    fig.update_layout(
        template="plotly_white"
    )

    return fig