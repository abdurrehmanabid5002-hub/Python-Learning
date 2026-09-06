import random
import time
from collections import defaultdict

def quantum_butterfly_effect(seed_text, iterations=5, chaos_factor=0.3):
    """
    A chaotic text evolution simulator inspired by quantum superposition and butterfly effect.
    Each character exists in multiple states simultaneously until 'observed'.
    """
    # Quantum state initialization
    quantum_states = defaultdict(lambda: list('abcdefghijklmnopqrstuvwxyz '))
    quantum_states[' '] = list(' ')
    quantum_states['.'] = list('.!?')
    
    # Seed the quantum field
    text = seed_text.lower()
    history = [text]
    
    for i in range(iterations):
        # Quantum decoherence - each character collapses to a new state
        new_text = []
        for char in text:
            if char in quantum_states:
                # Superposition collapse with chaos influence
                possible_states = quantum_states[char]
                if random.random() < chaos_factor:
                    # Butterfly effect: small change causes massive deviation
                    new_char = random.choice(possible_states + list('aeiou'))
                else:
                    new_char = random.choice(possible_states)
                new_text.append(new_char)
            else:
                new_text.append(char)
        
        text = ''.join(new_text)
        
        # Entanglement: propagate changes through the text
        if i > 0 and len(text) > 10:
            # Quantum entanglement - change propagates
            entanglement_point = random.randint(0, len(text)-1)
            for j in range(entanglement_point, min(entanglement_point + 5, len(text))):
                if random.random() < 0.4:
                    text = text[:j] + random.choice('abcdefghijklmnopqrstuvwxyz') + text[j+1:]
        
        history.append(text)
        time.sleep(0.5)  # Dramatic pause between iterations
    
    return history

# Multi-verse simulation
def multiverse_collapse():
    print("🌌 QUANTUM BUTTERFLY EFFECT SIMULATOR 🌌")
    print("=" * 50)
    
    seed = "the butterfly flapped its wings in the quantum void"
    print(f"Original timeline: {seed}\n")
    
    # Generate multiple parallel universes
    universes = []
    for universe_id in range(3):
        print(f"🪐 Observing Universe {universe_id + 1}...")
        timeline = quantum_butterfly_effect(seed, iterations=4, chaos_factor=0.3 + universe_id * 0.1)
        universes.append(timeline)
        
        for step, state in enumerate(timeline):
            print(f"  t={step}: {state}")
        print("-" * 40)
    
    # Quantum observer effect - final collapse
    print("\n🔮 FINAL QUANTUM COLLAPSE 🔮")
    final_universe = random.choice(universes)[-1]
    
    # Recursive fractal expansion
    def fractal_expand(text, depth=0):
        if depth > 3:
            return text
        expanded = []
        for char in text:
            if char == ' ' and random.random() < 0.3:
                expanded.append(' ' + fractal_expand('~' * random.randint(1, 3), depth+1))
            else:
                expanded.append(char)
        return ''.join(expanded)
    
    print(f"Observed reality: {final_universe}")
    print(f"Fractal echo: {fractal_expand(final_universe)}")
    
    # Entropy measurement
    entropy = sum(ord(c) for c in final_universe) % 100
    print(f"🌊 Entropy signature: {entropy}% chaotic")
    
    return final_universe

if __name__ == "__main__":
    result = multiverse_collapse()