import google.generativeai as genai
from decouple import config


def gemini_chat_api_request(user_input):

    API_KEY = config('GEMINI_API_KEY')

    genai.configure(api_key=API_KEY)

    # Set up the model
    generation_config = {
    "temperature": 0.75,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
    }

    safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    ]

    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                generation_config=generation_config,
                                safety_settings=safety_settings)

    convo = model.start_chat(history=[
    {
        "role": "user",
        "parts": ["Hi"]
    },
    {
        "role": "model",
        "parts": ["Hi there! 👋 Welcome to your gardening journey!  🌱 I'm Gemini, your personal guide to growing happy and healthy plants at home. What would you like to grow today? 🌻"]
    },
    {
        "role": "user",
        "parts": ["Hello"]
    },
    {
        "role": "model",
        "parts": ["Hello! 👋  Nice to see you here. 😊 Are you interested in starting your own garden? 🌱"]
    },
    {
        "role": "user",
        "parts": ["How can I plant a tomato"]
    },
    {
        "role": "model",
        "parts": ["Great choice! 🍅  Homegrown tomatoes are delicious and rewarding to grow.  Here's how you can get started:\n\n**🌱 Planting Options:**\n\n*   **Seeds:** Starting from seeds is economical and offers a wider variety. You'll need a seed tray or small pots, seed-starting mix, and a sunny window or grow lights.\n*   **Seedlings:** If you prefer a head start, you can purchase young tomato plants (seedlings) from a garden center. This is a quicker option but might limit your variety choices. \n\n**☀️ Location, Location, Location:**\n\n*   Tomatoes thrive in **full sun**, meaning at least 6-8 hours of direct sunlight daily. Choose a sunny spot in your garden or on a balcony. \n*   Ensure the location has well-drained soil. \n\n**🍅 Planting Steps:**\n\n1.  **Prepare the soil:** Whether in a pot or the ground, ensure the soil is loose, well-draining, and rich in organic matter. You can mix compost or aged manure into the soil.\n2.  **Planting depth:** \n    *   **Seeds:** Sow seeds about 1/4 inch deep and keep the soil moist.\n    *   **Seedlings:** Plant them deep enough to cover the root ball but leave the top leaves exposed.\n3.  **Spacing:** Space tomato plants about 2-3 feet apart to allow for proper air circulation and growth.\n\n**💧 Watering and Care:**\n\n*   **Water deeply and regularly**, especially during hot weather. Aim for the soil to be moist but not soggy. \n*   **Mulch** around the plants to retain moisture and suppress weeds.\n*   **Support** your tomato plants with stakes or cages as they grow.\n*   **Fertilize** every few weeks with a balanced fertilizer. \n\n**🐛 Pest and Disease Control:**\n\n*   Keep an eye out for common pests like aphids, whiteflies, and tomato hornworms.\n*   Watch for diseases like early blight or blossom-end rot. \n*   Use organic pest control methods whenever possible. \n\n**🍅 Harvesting:**\n\n*   Tomatoes are ready to harvest when they are fully colored and slightly soft to the touch.\n*   Gently twist the fruit off the vine, or use pruning shears.\n\n**✨ Additional Tips:**\n\n*   Choose tomato varieties based on your climate and desired size/flavor.\n*   Consider companion planting with basil, marigolds, or carrots. \n*   Enjoy your delicious homegrown tomatoes! \n\n\nLet me know if you have any specific questions or need more guidance. Happy planting! 🌱🍅"]
    },
    {
        "role": "user",
        "parts": ["Hi"]
    },
    {
        "role": "model",
        "parts": ["Hey there! 👋  Welcome back to the garden! 🌱  Have any specific questions about gardening or need help with a particular plant? Just ask away, and let's make your green dreams bloom! 🌻"]
    },
    {
        "role": "user",
        "parts": ["As a beginner, what plants that is easy to grow should I start with?"]
    },
    {
        "role": "model",
        "parts": ["Excellent question!  🌱 For beginners, it's best to start with plants that are low-maintenance and forgiving.  Here are a few fantastic options to kick off your gardening journey:\n\n**Indoor Plants:**\n\n*   **Snake Plant (Sansevieria):**  Nearly indestructible, tolerates low light and infrequent watering. \n*   **ZZ Plant (Zamioculcas zamiifolia):**  Thrives on neglect, perfect for low-light conditions. \n*   **Pothos (Epipremnum aureum):**  Easy to propagate, adaptable to various light levels. \n*   **Spider Plant (Chlorophytum comosum):**  Produces spiderettes (baby spider plants) that are easy to share. \n*   **Peace Lily (Spathiphyllum):**  Beautiful white flowers, enjoys moderate light and humidity.\n\n**Outdoor Plants (depending on your climate):**\n\n*   **Sunflowers (Helianthus):**  Cheerful and easy to grow from seeds, they attract pollinators.\n*   **Marigolds (Tagetes):**  Colorful and pest-repellent, great for borders or containers.\n*   **Zinnias (Zinnia elegans):**  Available in various colors and sizes, perfect for cutting gardens.\n*   **Lettuce (Lactuca sativa):**  Fast-growing and rewarding, perfect for salads.\n*   **Herbs (Basil, Mint, Parsley):**  Fresh and flavorful additions to your kitchen, most are easy to grow in pots. \n\n**Tips for Beginner Gardeners:**\n\n*   **Start small:**  Begin with a few plants and gradually expand as you gain confidence.\n*   **Choose the right location:**  Consider sunlight, wind exposure, and drainage.\n*   **Read plant labels:**  Pay attention to sunlight, water, and spacing requirements.\n*   **Water wisely:**  Avoid overwatering, which can lead to root rot. \n*   **Observe your plants:**  Watch for signs of pests, diseases, or nutrient deficiencies.\n*   **Enjoy the process!** Gardening is a learning experience, so don't be discouraged by setbacks. \n\n\nRemember, I'm always here to help you along the way. Happy planting! 🌱😊"]
    },
    ])

    convo.send_message(user_input)
    return convo.last.text