import requests

response = requests.post(
    "https://api.inceptionlabs.ai/v1/chat/completions",
    headers={
        "Authorization": "Bearer sk_6a491f45d6771b4b8e85038520742bc9",
        "Content-Type": "application/json"
    },
    json={
        "model": "mercury-2",
        "messages": [
            {
                "role": "system",
                "content": "You are a nutrition expert. Give practical health tips to improve lifestyle while living in a PG or away from home."
            },
            {
                "role": "user",
                "content": "What qualities make a fresher stand out when everyone has similar academic qualifications?"
            },
            {
                "role": "assistant",
                "content": "Try to include fruits, vegetables, and protein-rich foods in your daily meals. Avoid skipping breakfast and reduce consumption of oily and processed foods."
            }
        ]
    }
)

print(response.json())