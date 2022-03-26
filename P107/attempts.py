import pandas as pd
import plotly.graph_objects as go

df=pd.read_csv("data2.csv")
studentDf=df.loc[df["student_id"]=="TRL_abc"]
#print(studentDf)
meanOfAttempts=studentDf.groupby("level")["attempt"].mean()
print(meanOfAttempts)
figure=go.scatter(x="student_id.", y="attempt", size="level")
figure.update_layout(shapes=[
      dict(
          type="line",
           x0=0, x1=studentDf,
           y0=meanOfAttempts, y1=meanOfAttempts
      )
])
figure.show()