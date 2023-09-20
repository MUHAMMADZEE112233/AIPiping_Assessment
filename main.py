import fastapi
import openai

app = fastapi.FastAPI()

openai.api_key = "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"

@app.get("/recommendations")
async def get_recommendations(country: str, season: str):
 
  if season not in ["summer", "fall", "winter", "spring"]:
    raise fastapi.HTTPException(status_code=400, detail="Invalid season.")

  prompt = f"Write a list of three things to do in {country} during the {season}."

  response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=100,
  )

  recommendations = response.choices[0].text.split("\n")

  return {
    "country": country,
    "season": season,
    "recommendations": recommendations
  }
