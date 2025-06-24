import io
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse
import uvicorn

plt.rc('font', family='AppleGothic')
plt.rc('axes', unicode_minus=False)

app = FastAPI()

def load_data(crop_path="data/crop.csv", weather_path="data/weather.csv", location="Busan"):
    crop = pd.read_csv(crop_path)
    crop = crop[crop['year'].apply(lambda x: str(x).isdigit())]
    crop['year'] = crop['year'].astype(int)
    crop = crop.rename(columns={'avg': 'production'})
    weather = pd.read_csv(weather_path)
    weather['year'] = weather['year'].astype(int)
    weather = weather.rename(columns={'avg': 'temp_avg'})
    weather = weather[weather['location'] == location]
    df = pd.merge(
        crop[['year','production']],
        weather[['year','temp_avg']],
        on='year', how='inner'
    ).sort_values('year')
    return df

def create_rice_vs_weather_png(df):
    buf = io.BytesIO()
    fig, ax1 = plt.subplots(figsize=(10,6))
    ax1.plot(df['year'], df['production'], '-o', color='tab:blue', label='생산량')
    ax1.set_xlabel("연도")
    ax1.set_ylabel("생산량 (원)", color='tab:blue')
    ax1.tick_params(axis='y', labelcolor='tab:blue')
    ax1.grid(alpha=0.3)
    ax2 = ax1.twinx()
    ax2.scatter(df['year'], df['temp_avg'], color='tab:red', s=80, label='평균 기온')
    ax2.set_ylabel("평균 기온 (℃)", color='tab:red')
    ax2.tick_params(axis='y', labelcolor='tab:red')
    fig.tight_layout()
    fig.savefig(buf, format='png', dpi=300)
    plt.close(fig)
    buf.seek(0)
    return buf.read()

@app.get("/", response_class=HTMLResponse)
def index():
    return """
    <html>
      <head>
        <meta charset="utf-8"/>
        <title>Farmcast Dashboard</title>
        <style>
          body { font-family: 'AppleGothic', sans-serif; margin: 0; padding: 0; background: #f4f7fa; color: #333; }
          .container { max-width: 900px; margin: 40px auto; padding: 20px; background: #fff; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
          h1 { text-align: center; font-size: 2em; margin-bottom: 0.5em; }
          h2 { font-size: 1.2em; margin-top: 1.5em; color: #555; }
          .chart { text-align: center; margin-top: 10px; }
          img { max-width: 100%; border: 1px solid #ddd; border-radius: 4px; }
        </style>
      </head>
      <body>
        <div class="container">
          <h1>Farmcast Dashboard</h1>
          <h2>쌀 생산량 vs 평균 기온</h2>
          <div class="chart">
            <img src="/plot/rice_vs_weather.png" alt="Rice vs Weather"/>
          </div>
        </div>
      </body>
    </html>
    """

@app.get("/plot/rice_vs_weather.png")
def rice_vs_weather_image():
    df = load_data()
    return Response(create_rice_vs_weather_png(df), media_type="image/png")

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)