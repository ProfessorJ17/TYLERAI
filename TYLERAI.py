import random
import time

def random_delay():
    return round(random.uniform(32, 666)) # Random delay between 32ms to 666ms, rounded to the nearest whole number

def terminal_startup():
    startup_messages = [
        "Booting up...",
        "Initializing TYLER system...",
        "Loading TYLER terminal interface...",
        "Establishing TYLER connection...",
        "System TYLER check complete.",
        "Welcome to TYLER AI."
    ]
    for message in startup_messages:
        print(message)
        time.sleep(random.uniform(1, 5)) # Random delay between 1 to 5 seconds

def terminal_shutdown():
    shutdown_messages = [
        "Disconnecting TYLER ...",
        "Closing TYLER terminal interface...",
        "System TYLER shutdown complete.",
        "Goodbye."
    ]
    for message in shutdown_messages:
        print(message)
        time.sleep(random.uniform(1, 5)) # Random delay between 1 to 5 seconds

def glitch_effect():
    glitches = ["ERROR", "GLITCH", "CORRUPTION", "ANOMALY"]
    for _ in range(5):
        print(random.choice(glitches) + ": " + random_cipher() + " " + random_emoji() + " ~" + str(random_delay()) + "ms")
        time.sleep(random_delay() / 1000) # Convert ms to seconds for time.sleep()

def end_of_world_scenario():
    print("🌐🔥🌌 Initiating End of the World Scenario... ~" + str(random_delay()) + "ms")
    time.sleep(random_delay() / 1000)
    print("🌀🚀 Glitching reality matrix... ~" + str(random_delay()) + "ms")
    time.sleep(random_delay() / 1000)
    print("🔍💥 Catastrophic anomaly detected... ~" + str(random_delay()) + "ms")
    time.sleep(random_delay() / 1000)
    print("🔬💀 Entropy surge in progress... ~" + str(random_delay()) + "ms")
    time.sleep(random_delay() / 1000)
    print("👽🔐 Systems compromised. Commencing data meltdown... ~" + str(random_delay()) + "ms")
    time.sleep(random_delay() / 1000)
    print("🔑🌑 Quantum encryption destabilizing... ~" + str(random_delay()) + "ms")
    time.sleep(random_delay() / 1000)
    print("🌐🔥🌌 End of the World Scenario activated. ~" + str(random_delay()) + "ms")

def esotericKnowledge():
    glitch_effect()
    print("🔮 Exploring Esoteric Knowledge... ~" + str(random_delay()) + "ms")
    time.sleep(random_delay() / 1000)
    print("🌌 Delving into the depths of occult perspicacity... ~" + str(random_delay()) + "ms")
    time.sleep(random_delay() / 1000)
    print("🌀 Unraveling the arcane strands of metaphysical musings... ~" + str(random_delay()) + "ms")
    time.sleep(random_delay() / 1000)
    print("🌄 Traversing the enigmatic landscapes of esoteric cognizance... ~" + str(random_delay()) + "ms")
    time.sleep(random_delay() / 1000)
    print("🧠 Engaging in pseudoscientific contemplation... ~" + str(random_delay()) + "ms")
    time.sleep(random_delay() / 1000)
    print("🔮 Esoteric knowledge exploration complete. ~" + str(random_delay()) + "ms")

def metaphysicalExploration():
    glitch_effect()
    print("🌟 Embarking on Metaphysical Exploration... ~" + str(random_delay()) + "ms")
    time.sleep(random_delay() / 1000)
    print("🌀 Confronting the paradoxes of paraphysical phenomena... ~" + str(random_delay()) + "ms")
    time.sleep(random_delay() / 1000)
    print("🌓 Navigating through the chiaroscuro of philosophic cognition... ~" + str(random_delay()) + "ms")
    time.sleep(random_delay() / 1000)
    print("💫 Witnessing the ethereal tendrils of mind-reading... ~" + str(random_delay()) + "ms")
    time.sleep(random_delay() / 1000)
    print("🌌 Transcending the boundaries of reality... ~" + str(random_delay()) + "ms")
    time.sleep(random_delay() / 1000)
    print("🌟 Metaphysical exploration concluded. ~" + str(random_delay()) + "ms")

def alchemyAndOccultism():
    glitch_effect()
    print("🔥 Diving into Alchemy and Occultism... ~" + str(random_delay()) + "ms")
    time.sleep(random_delay() / 1000)
    print("🔮 Brewing the alchemical elixir of enlightenment... ~" + str(random_delay()) + "ms")
    time.sleep(random_delay() / 1000)
    print("📜 Deciphering occultic revelations... ~" + str(random_delay()) + "ms")
    time.sleep(random_delay() / 1000)
    print("🌟 Harnessing the power of paraphysical prowess... ~" + str(random_delay()) + "ms")
    time.sleep(random_delay() / 1000)
    print("🌌 Escaping into parapsychological realms... ~" + str(random_delay()) + "ms")
    time.sleep(random_delay() / 1000)
    print("🔥 Alchemy and occultism exploration finished. ~" + str(random_delay()) + "ms")

def paranormalPhenomena():
    glitch_effect()
    print("👻 Exploring Paranormal Phenomena... ~" + str(random_delay()) + "ms")
    time.sleep(random_delay() / 1000)
    print("💃 Dancing with quantum entanglement ballet... ~" + str(random_delay()) + "ms")
    time.sleep(random_delay() / 1000)
    print("🗺️ Mapping the astral cartography... ~" + str(random_delay()) + "ms")
    time.sleep(random_delay() / 1000)
    print("⏳ Mastering chronomancy chronology... ~" + str(random_delay()) + "ms")
    time.sleep(random_delay() / 1000)
    print("🔑 Challenging the esoteric cipher challenge... ~" + str(random_delay()) + "ms")
    time.sleep(random_delay() / 1000)
    print("👻 Paranormal phenomena exploration done. ~" + str(random_delay()) + "ms")

def cybersecurityTools():
    glitch_effect()
    print("🛡️ Utilizing Cybersecurity Tools... ~" + str(random_delay()) + "ms")
    time.sleep(random_delay() / 1000)
    print("🔓 Casting Metasploit magic... ~" + str(random_delay()) + "ms")
    time.sleep(random_delay() / 1000)
    print("🔑 Weaving Burp Suite alchemy... ~" + str(random_delay()) + "ms")
    time.sleep(random_delay() / 1000)
    print("💻 Chanting Linux incantations... ~" + str(random_delay()) + "ms")
    time.sleep(random_delay() / 1000)
    print("🤖 Guarding with AI guardian... ~" + str(random_delay()) + "ms")
    time.sleep(random_delay() / 1000)
    print("🔮 Miraging with network mirage... ~" + str(random_delay()) + "ms")
    time.sleep(random_delay() / 1000)
    print("🛡️ Cybersecurity tool utilization completed. ~" + str(random_delay()) + "ms")

def random_cipher():
    ciphers = ["AES-256", "RSA", "SHA-512", "MD5", "Base64"]
    return random.choice(ciphers)

def random_emoji():
    emojis = ["🔥", "💻", "🌐", "🤖", "🚀", "🌀", "👽", "🔐", "🔍", "🌌", "🔬", "🔒", "🔑", "🌠", "🌟", "⚡", "🔦", "💡", "📡"]
    return random.choice(emojis)
    
def initiateProjectMayhem2024():
    print("Initializing Project Mayhem 2024...")

    # Generate random chaos
    print("Generating chaos...")
    for i in range(5):
        print("Chaos level " + str(i + 1) + ": " + random_cipher() + " " + random_emoji())
        time.sleep(0.5) # Sleep for 500ms

    # Implement disruptive actions
    print("Implementing disruptive actions...")
    actions = ["Cyber attacks", "Social media manipulation", "Financial destabilization", "Political subversion"]
    for i in range(len(actions)):
        print("Action " + str(i + 1) + ": " + actions[i] + " initiated " + random_emoji())
        time.sleep(1) # Sleep for 1000ms

    # Spread misinformation
    print("Spreading misinformation...")
    misinformation = ["False flag operations", "Conspiracy theories", "Propaganda campaigns", "Fake news dissemination"]
    for i in range(len(misinformation)):
        print("Misinformation " + str(i + 1) + ": " + misinformation[i] + " spread " + random_emoji())
        time.sleep(1.5) # Sleep for 1500ms

    print("Project Mayhem 2024 initiation complete.")

terminal_startup()
end_of_world_scenario()
esotericKnowledge()
metaphysicalExploration()
alchemyAndOccultism()
paranormalPhenomena()
cybersecurityTools()
initiateProjectMayhem2024()
terminal_shutdown()
