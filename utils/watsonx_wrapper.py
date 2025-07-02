from ibm_watsonx_ai.foundation_models import Model
from ibm_watsonx_ai import IAMTokenManager

# ✅ Replace these placeholders with your actual IBM Watsonx credentials
API_KEY = "your-ibm-cloud-api-key"
PROJECT_ID = "your-watsonx-project-id"
MODEL_ID = "granite-20b-multilingual"  # Default model name

def call_watsonx(prompt):
    try:
        # Authenticate with IBM Watsonx
        token_manager = IAMTokenManager(api_key=API_KEY)
        model = Model(
            model_id=MODEL_ID,
            token_manager=token_manager,
            project_id=PROJECT_ID
        )

        # Send prompt to Granite model
        result = model.generate_text(
            prompt=prompt,
            max_new_tokens=200  # adjust if you want longer/shorter output
        )

        # Return the generated response
        return result['results'][0]['generated_text']

    except Exception as e:
        return f"Watsonx Error: {str(e)}"
