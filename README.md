# **🏕️ Camping Spot Finder**

Welcome to the **Camping Spot Finder**. This repository contains the strategic instructions and data structures needed to turn any advanced AI chat agent into an automated off-grid scouting assistant.

Currently optimized for overland trips in a 4x4 Tacoma with a Starlink Mini, this system evaluates spots based on a rigorous matrix including cost, water access, beauty, cellular connectivity, and bear risk.

## **🚀 How to Use (The "No-Code" Workflow)**

This system operates entirely through an AI chat interface. Follow these simple steps to generate your camping spots:

### **Step 1: Package the Context**

*(Prerequisite: If you don't have Repomix installed, you will need Node.js installed on your machine. You can then install Repomix globally by running npm install \-g repomix in your terminal).*

In your terminal, navigate to the root directory of this repository and run [Repomix](https://github.com/yamadashy/repomix) to bundle the system instructions.

repomix

*This will generate a file named context\_digest\_camp\_spot\_finder.xml in your audit/ folder (or your configured output directory).*

### **Step 2: Initialize the AI Agent**

1. Open your preferred AI chat interface (e.g., Gemini, Claude, ChatGPT).  
2. Upload the context\_digest\_camp\_spot\_finder.xml file.  
3. Include the prompt instructions from agents.md to initialize the agent's behavior.

### **Step 3: Prompt for Locations**

Simply ask the AI for a location:

*"Generate spots for Black Canyon of the Gunnison National Park."*

### **Step 4: Save Your Files**

The AI will immediately process the request and return the best "Geo-Cluster" (a group of campsites within a 5-mile driving radius).

1. **Create the Folder:** The AI will provide a file path like src/spots/Black\_Canyon/South\_Rim\_Dispersed/. Create this folder in your local directory.  
2. **Copy and Paste:** The AI will output perfectly formatted .yaml files for each campsite. Copy and paste these code blocks into their respective files within your new folder.

## **💡 Pro-Tip: Filtering Out Old Locations**

As your trips progress, you will accumulate dozens of saved YAML files. To keep your AI context lean, cheap, and focused strictly on your *next* destination, you should tell Repomix to ignore regions you've already visited.

Open the repomix.config.json file in the root of your repository and add the old target area's path to the customPatterns array under ignore.

For example, to ignore all the spots you already saved in Moab, adjust your config like this:

{  
    "ignore": {  
        "customPatterns": \[  
            "\*\*/\*context\_digest\*.xml",  
            "\*\*/siminterepomix\*.xml",  
            "\*\*/project\_skeleton\*.txtModuleState.yaml",  
            ".git/\*\*",  
            "node\_modules/\*\*",  
            "\*\*/design/.proposals",  
            "src/spots/Moab\_BLM/\*\*"   
        \]  
    }  
}

*After saving the config, just run repomix again, and those old locations will be cleanly excluded from your new digest\!*

## **🛠️ Personalizing Your Setup (Strategy.yaml)**

The default instructions are tailored for a 4x4 Tacoma with a Starlink Mini. However, you can easily customize the AI's scoring logic to match your specific vehicle and gear\!

Open the strategy/Strategy.yaml file. Here, you can adjust the objective and modify the evaluation\_matrix descriptions and weights.

For example, if you are traveling in a **Tesla** and rely on cellular service rather than Starlink, you might update the criteria like this:

objective: "Scout, evaluate, and organize camping locations near set GPS coordinates for a road trip in a Tesla Model Y."

\# ... inside the evaluation\_matrix / criteria section ...

    \- name: "Connectivity"  
      weight: 1.0  
      description: "Cell service viability. 7 is full 5G/LTE, 1 is a complete dead zone."  
    \- name: "Road Accessibility"  
      weight: 2.0  
      description: "Tesla Model Y viability. 1 requires high-clearance 4x4 or is heavily washed out, 7 is fully paved directly to the spot."

*Once you save your changes, just run repomix again to update your context digest with your newly personalized strategy\!*

## **⚠️ Under the Hood: The 95% Solution**

**Note on LIXA Architecture:** If you browse the repository, you will notice references to the **LIXA** (LLM Interactive Execution Agent) framework, Strategy.yaml, and interface.py.

Currently, the underlying code execution elements (the "Maker" and "Verifier" agents that would physically write these files to your hard drive) are **disconnected**. The Python code elements of this module are not yet fully built out.

**Why use it like this?** This is a prime example of the **Pareto Principle** (the 80/20 rule) pushed to a **95% solution**. By utilizing a loose, flexible "drop into chat" method, the AI's natural reasoning capabilities seamlessly fill in the gaps of the missing code. You get 95% of the value of a fully automated scouting application with zero maintenance, zero API keys, and zero debugging. The AI acts as the application layer.