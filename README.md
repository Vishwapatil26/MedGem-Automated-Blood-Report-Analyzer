**Overview**

MedGem is a powerful tool designed to automate the extraction and interpretation of data from medical blood reports. The project was developed as part of the Gemini API Competition. It utilizes advanced AI models to analyze medical images, particularly blood reports, and provide relevant health advice based on the extracted data.

**Key Features**

- Automated Data Extraction: MedGem uses the Gemini AI model to efficiently extract information from medical blood reports.
- Image Analysis: The tool can analyze uploaded images of medical reports to identify and interpret key data points.
- Customizable Prompts: Users can input specific questions or prompts related to the medical report, and MedGem will provide accurate responses based on the image content.
- Health Advice: Depending on the questions asked, MedGem can also provide health advice based on the data extracted from the report.

**How It Works**

1. User Input: The user provides a text input prompt that specifies what they want to know about the blood report.
2. Image Upload: The user uploads an image of the medical report (e.g., a blood test result).
3. Processing: MedGem uses the Gemini AI model to analyze the image, extract the necessary information, and generate a response based on the input prompt.
4. Output: The tool displays the extracted data and any relevant health advice.   

**How to Use**

1. Set Up Environment: Ensure that your environment is configured with the necessary dependencies. You need to have a Google API key for the Gemini AI model.
2. Run the Application: Use a platform like Streamlit to run the MedGem application.
3. Input Prompt: Enter a specific prompt or question in the provided input field.
4. Upload Image: Upload the image of the medical report you want to analyze.
5. Get Results: Click the button to process the image, and MedGem will display the relevant information and advice.   

**Technical Details**   
- Languages and Libraries: The project is built using Python, Streamlit for the web interface, and the PIL library for image processing.   
- AI Model: MedGem uses the Gemini 1.5 Flash AI model for content generation and data extraction.   
- Environment Variables: The Google API key is managed using environment variables for security purposes.   
