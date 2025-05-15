# Use the official Rasa SDK image as base
FROM rasa/rasa-sdk:3.1.2

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose ports
EXPOSE 5005

# Start the action server
CMD ["rasa", "run", "--enable-api", "--cors", "*", "--debug"]