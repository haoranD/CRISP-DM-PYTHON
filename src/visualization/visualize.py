import data

data.Import_Packages

def gender_pie(singlefile):
    singlefile = singlefile[singlefile['gender'] != 'Unknown']

    print('The other genders are just occupy a very little,so we do not need to consider them temporarily')
    print('Proportions of the male and female tend to balance.')
    print('The differences between male and female we can asuume that male have more interests in this kind of course.')

    labels = ['Female','Male','Other']
    values = [float(len(singlefile[singlefile['gender'] == 'female'])) / float(len(singlefile['gender'])) ,
                float(len(singlefile[singlefile['gender'] == 'male'])) / float(len(singlefile['gender'])) ,
                float(len(singlefile[singlefile['gender'] == 'other'])) / float(len(singlefile['gender']))]

    trace = go.Pie(labels=labels, values=values)

    py.iplot([trace], filename='basic_pie_chart')


def country_bar(singlefile):
    singlefile = singlefile[singlefile['detected_country'] != 'Unknown']
    country = singlefile['detected_country']

    re = pd.value_counts(country)

    re_vale = re.tolist()[0:20]
    re_name = re.index.tolist()[0:20]
    print('Chosing tweenty countries(Number of students in other countries are too small to represent) to check the Population ')



    trace0 = go.Bar(
        x=re_name,
        y=re_vale,
        marker=dict(
            color='rgb(158,202,225)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5,
            )
        ),
        opacity=0.6
    )

    data = [trace0]
    layout = go.Layout(
        title='Different Countries Students in Term 7',
    )

    fig = go.Figure(data=data, layout=layout)
    py.iplot(fig, filename='text-hover-bar')


def country_pie(fileName1, fileName2):
    pie1 = pd.read_csv(fileName1)
    pie1 = pie1[pie1['detected_country'] != 'Unknown']
    pie1 = pie1['detected_country']

    re = pd.value_counts(pie1)

    re_vale1 = re.tolist()[0:20]
    re_name1 = re.index.tolist()[0:20]
    

    pie2 = pd.read_csv(fileName2)
    pie2 = pie2[pie2['detected_country'] != 'Unknown']
    pie2 = pie2['detected_country']

    re = pd.value_counts(pie2)

    re_vale2 = re.tolist()[0:20]
    re_name2 = re.index.tolist()[0:20]

    fig = {
    "data": [
        {
        "values": re_vale1,
        "labels": re_name1,
        "domain": {"x": [0, .48]},
        "name": "Term 6",
        "hoverinfo":"label+percent+name",
        "hole": .4,
        "type": "pie"
        },
        {
        "values": re_vale2,
        "labels": re_name2,
        "textposition":"inside",
        "domain": {"x": [.52, 1]},
        "name": "Term 7",
        "hoverinfo":"label+percent+name",
        "hole": .4,
        "type": "pie"
        }],
    "layout": {
            "title":"Percentage of students come from",
            "annotations": [
                {
                    "font": {
                        "size": 20
                    },
                    "showarrow": False,
                    "text": "Term 6",
                    "x": 0.20,
                    "y": 0.5
                },
                {
                    "font": {
                        "size": 20
                    },
                    "showarrow": False,
                    "text": "Term 7",
                    "x": 0.8,
                    "y": 0.5
                }
            ]
        }
    }
    py.iplot(fig, filename='donut')


def answer_line(singlefile):
    numF = len(singlefile[singlefile['correct'] == False])
    numT = len(singlefile[singlefile['correct'] == True])

    question = pd.unique(singlefile['quiz_question'])

    WrongAnswer = []

    choose_tmp = singlefile[singlefile['correct'] == False]

    for i in question:
        WrongAnswer.append(len(choose_tmp[choose_tmp['quiz_question'] == i]))

    # Create traces
    trace0 = go.Scatter(
        x = question,
        y = WrongAnswer,
        mode = 'lines+markers',
        name = 'lines+markers'
    )
    data = [trace0]

    py.iplot(data, filename='line-mode')

def Treemap(singlefile):
    reasons = pd.unique(singlefile['leaving_reason'])

    reasons = reasons.tolist()
    re_va = []

    for i in reasons:
        re_va.append(len(singlefile[singlefile['leaving_reason'] == i]))    
        dict_reasons = dict(zip(reasons,re_va))

    invalid_data = list(range(int((1/5) * max(re_va))))

    for i in reasons:
        if dict_reasons[i] in invalid_data:
            dict_reasons.pop(i)
        
    reasons = list(dict_reasons.keys())
    re_va = list(dict_reasons.values())

    x = 0.
    y = 0.
    width = 100.
    height = 100.

    values = re_va

    normed = squarify.normalize_sizes(values, width, height)
    rects = squarify.squarify(normed, x, y, width, height)

    # Choose colors from http://colorbrewer2.org/ under "Export"
    color_brewer = ['rgb(166,206,227)','rgb(31,120,180)','rgb(178,223,138)',
                    'rgb(51,160,44)','rgb(251,154,153)','rgb(227,26,28)']
    shapes = []
    annotations = []
    counter = 0

    for r in rects:
        shapes.append( 
            dict(
                type = 'rect', 
                x0 = r['x'], 
                y0 = r['y'], 
                x1 = r['x']+r['dx'], 
                y1 = r['y']+r['dy'],
                line = dict( width = 2 ),
                fillcolor = color_brewer[counter]
            ) 
        )
        annotations.append(
            dict(
                x = r['x']+(r['dx']/2),
                y = r['y']+(r['dy']/2),
                text = reasons[counter],
                showarrow = False
            )
        )
        counter = counter + 1
        if counter >= len(color_brewer):
            counter = 0

    # For hover text
    trace0 = go.Scatter(
        x = [ r['x']+(r['dx']/2) for r in rects ], 
        y = [ r['y']+(r['dy']/2) for r in rects ],
        text = [ str(v) for v in reasons ], 
        mode = 'text',
    )
        
    layout = dict(
        height=950, 
        width=950,
        xaxis=dict(showgrid=False,zeroline=False),
        yaxis=dict(showgrid=False,zeroline=False),
        shapes=shapes,
        annotations=annotations,
        hovermode='closest'
    )

    figure = dict(data=[trace0], layout=layout)

    py.iplot(figure, filename='squarify-treemap')