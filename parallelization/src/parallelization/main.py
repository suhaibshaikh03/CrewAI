from crewai.flow.flow import Flow, start, listen, or_, and_
from litellm import completion
import time

class ParallelFlow(Flow):
    model = "gemini/gemini-1.5-flash"

    @start()
    def generate_variant_1(self):
        response = completion(
            model=self.model,
            messages=[{"role": "user", "content": "Generate a topic in world of ai. just return a single word."}]
        )
        variant = response["choices"][0]["message"]["content"].strip()
        print(f"Variant 1: {variant}")
        print("---------------------------------------------------------------------------")
        
        return variant

    @start()
    def generate_variant_2(self):
        response = completion(
        model=self.model,
        messages=[{"role": "user", "content": "Generate a topic in world of blockchain. just return a single word."}]

        )
        
        variant = response["choices"][0]["message"]["content"].strip()
        print(f"Variant 2: {variant}")
        print("---------------------------------------------------------------------------")
        return variant

    @listen(or_(generate_variant_1, generate_variant_2))
    def aggregate_variants(self, variant):
        # For simplicity, print the first variant received.
        print("Aggregated Variant:")
    
        print(variant)
        print("---------------------------------------------------------------------------")
        return variant

def kickoff():
    flow = ParallelFlow()
    final = flow.kickoff()
    print("Final Aggregated Output:")
    print(final)
