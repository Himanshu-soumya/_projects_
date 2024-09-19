#this file contain the data that will be shown in the webpages depending on the conditions like if we have NHigh that mean
# high nitrogen the it will suggest some steps to take for that
fertilizer_dict = {
    'NHigh': """<b style="color:#c79c60;">The soil has a high nitrogen (N) content, which may lead to weed growth.</b>
    <br/><br/> Please consider the following recommendations:
    <p align="justify">1. <i>Manure:</i> Adding manure is a simple way to amend the soil with nitrogen. Be cautious about the type of manure, as nitrogen levels can vary.</p>
    <p align="justify">2. <i>Coffee Grounds:</i> Utilize coffee grounds, a green compost material rich in nitrogen, which also improves soil drainage.</p>
    <p align="justify">3. <i>Nitrogen-Fixing Plants:</i> Plant vegetables from the Fabaceae family, such as peas and beans, to naturally increase nitrogen in the soil.</p>
    <p align="justify">4. Plant 'green manure' crops like cabbage, corn, and broccoli.</p>
    <p align="justify">5. <i>Mulch:</i> Use wet grass or other materials like sawdust for mulching while growing crops.</p><hr style="height:2px; background-color:#c79c60;">""",

    'Nlow': """<b style="color:#c79c60;">The nitrogen (N) level in the soil is low.</b>
    <br/><br/> Please consider the following suggestions:
    <p align="justify">1. <i>Add Sawdust or Woodchips:</i> Incorporate sawdust or fine woodchips to your soil, as the carbon content helps absorb excess nitrogen.</p>
    <p align="justify">2. <i>Nitrogen-Feeding Plants:</i> Plant crops like tomatoes, corn, broccoli, and spinach that thrive on nitrogen.</p>
    <p align="justify">3. <i>Watering:</i> Soak your soil to leach nitrogen deeper, reducing its availability for plants.</p>
    <p align="justify">4. <i>Sugar:</i> Limited studies suggest that adding sugar can potentially reduce nitrogen levels in the soil.</p>
    <p align="justify">5. Add composted manure to the soil.</p>
    <p align="justify">6. Plant nitrogen-fixing plants like peas or beans.</p>
    <p align="justify">7. <i>Use NPK Fertilizers with High N Value.</i></p>
    <p align="justify">8. <i>Do Nothing:</i> If plants are already thriving, letting them absorb nitrogen can naturally amend the soil for future crops.</p><hr style="height:2px; background-color:#c79c60;">""",

    'NNo': """<b style="color:#c79c60;">The nitrogen (N) value in the soil is optimal.</b><hr style="height:2px; background-color:#c79c60;">""",

    'PHigh': """<b style="color:#c79c60;">The phosphorus (P) value in the soil is high.</b>
    <br/><br/>Please consider the following recommendations:
    <p align="justify">1. <i>Avoid Adding Manure:</i> Manure, while rich in nutrients, often contains high levels of phosphorus. Limit its addition to reduce phosphorus levels.</p>
    <p align="justify">2. <i>Phosphorus-Free Fertilizer:</i> Use fertilizers with no phosphorus or low phosphorus content, allowing existing phosphorus to be utilized by plants.</p>
    <p align="justify">3. <i>Water Your Soil:</i> Soak the soil to drive phosphorus out, but this is a last-resort method.</p>
    <p align="justify">4. Plant nitrogen-fixing vegetables like beans and peas to increase nitrogen without raising phosphorus.</p>
    <p align="justify">5. Use crop rotations to decrease high phosphorus levels.</p><hr style="height:2px; background-color:#c79c60;">""",

    'Plow': """<b style="color:#c79c60;">The phosphorus (P) value in the soil is low.</b>
    <br/><br/>Please consider the following suggestions:
    <p align="justify">1. <i>Bone Meal:</i> A fast-acting source rich in phosphorus, made from ground animal bones.</p>
    <p align="justify">2. <i>Rock Phosphate:</i> A slower-acting source that needs soil conversion before plants can use phosphorus.</p>
    <p align="justify">3. <i>Phosphorus Fertilizers:</i> Apply fertilizers with high phosphorus content in the NPK ratio (e.g., 10-20-10).</p>
    <p align="justify">4. <i>Organic Compost:</i> Adding quality organic compost helps increase phosphorus content.</p>
    <p align="justify">5. <i>Manure:</i> Like compost, manure is an excellent source of phosphorus for plants.</p>
    <p align="justify">6. <i>Clay Soil:</i> Introduce clay particles to retain and fix phosphorus deficiencies.</p>
    <p align="justify">7. <i>Ensure Proper Soil pH:</i> Maintain a pH in the 6.0 to 7.0 range for optimal phosphorus uptake in plants.</p>
    <p align="justify">8. If soil pH is low, add lime or potassium carbonate. For high pH, add organic matter or acidifying fertilizers.</p><hr style="height:2px; background-color:#c79c60;">""",

    'PNo': """<b style="color:#c79c60;">The phosphorus (P) value in the soil is sufficient.</b><hr style="height:2px; background-color:#c79c60;">""",

    'KHigh': """<b style="color:#c79c60;">The potassium (K) value in your soil is high.</b>
    <br/><br/>Please consider the following recommendations:
    <p align="justify">1. <i>Loosen the Soil:</i> Deeply dig and water to dissolve water-soluble potassium. Repeat this process several times, allowing the soil to dry in between.</p>
    <p align="justify">2. <i>Sift Through the Soil:</i> Remove rocks, as minerals in rocks release potassium slowly through weathering.</p>
    <p align="justify">3. <i>Avoid Potassium-Rich Fertilizers:</i> Stop using fertilizers high in potassium. Opt for those with a '0' in the final number field in the NPK ratio.</p>
    <p align="justify">4. Mix crushed eggshells, seashells, wood ash, or soft rock phosphate into the soil for calcium and balance.</p>
    <p align="justify">5. Use NPK fertilizers with low potassium levels and organic fertilizers with low NPK values.</p>
    <p align="justify">6. Grow cover crops of legumes for nitrogen without increasing phosphorus or potassium.<hr style="height:2px; background-color:#c79c60;">""",

    'Klow': """<b style="color:#c79c60;">The potassium (K) value in your soil is low.</b>
    <br/><br/>Please consider the following suggestions:
    <p align="justify">1. Mix in muricate of potash or sulphate of potash.</p>
    <p align="justify">2. Try kelp meal or seaweed.</p>
    <p align="justify">3. Experiment with Sul-Po-Mag.</p>
    <p align="justify">4. Bury banana peels an inch below the soil's surface.</p>
    <p align="justify">5. Use Potash fertilizers, as they contain high levels of potassium.<hr style="height:2px; background-color:#c79c60;">
    """,

    'KNo': """<b style="color:#c79c60;">The potassium (K) value in your soil is satisfactory.</b><hr style="height:2px; background-color:#c79c60;">"""
}
