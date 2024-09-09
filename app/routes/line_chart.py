from flask import render_template
from app import app
from app.utils import load_data, generate_colors

@app.route('/line_chart')
def line_chart():
    table = load_data("dataset2.csv")
    labels = ['sisa lama', 'masuk', 'putus', 'sisa baru']
    
    datasets = []
    colors = generate_colors(len(table['PERKARA']))
    for index, perkara in enumerate(table['PERKARA']):
        data = table[table['PERKARA'] == perkara][labels].values.flatten().tolist()
        border_color = 'green' if perkara == 'Permohonan' else colors[index]
        datasets.append({
            "label": perkara,
            "data": data,
            "fill": False,
            "borderColor": border_color
        })

    chart_config = {
        "type": "line",
        "data": {
            "labels": labels,
            "datasets": datasets
        },
        "options": {
            "onClick": "function(event, array) { if(array.length > 0) { alert(array[0].element.$context.raw); } }"
        }
    }

    return render_template('line_chart.html', chart_config=chart_config)
