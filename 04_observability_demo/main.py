import os
import json
import time
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter
from opentelemetry.sdk.resources import Resource

# =========================
# Load ENV
# =========================
load_dotenv()

# =========================
# OpenTelemetry Setup
# =========================
resource = Resource(attributes={"service.name": "gemini-observability"})

trace.set_tracer_provider(TracerProvider(resource=resource))

span_processor = SimpleSpanProcessor(ConsoleSpanExporter())
trace.get_tracer_provider().add_span_processor(span_processor)

tracer = trace.get_tracer("gemini.agent")

# =========================
# Traced Function
# =========================
def traced_chain(question: str) -> str:
    with tracer.start_as_current_span("gemini_inference") as span:
        start_time = time.time()

        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0.7
        )

        span.set_attribute("model", "gemini-2.5-flash")
        span.set_attribute("question", question)

        response = llm.invoke(question)

        latency = time.time() - start_time

        log_entry = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "question": question,
            "response": response.content,
            "latency": f"{latency:.2f}s",
            "model": "gemini-2.5-flash"
        }

        print("\n📊 LOG:")
        print(json.dumps(log_entry, indent=2))

        return response.content

# =========================
# Run
# =========================
if __name__ == "__main__":
    try:
        query = "Explain quantum entanglement in simple terms"
        result = traced_chain(query)

        print("\n💎 FINAL RESPONSE:\n")
        print(result)

    except Exception as e:
        print(f"❌ Error: {str(e)}")