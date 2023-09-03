---

# 📊 Hierarchical Clustering Analysis on Product Reviews

### 📌 Table of Contents

1. [🌟 Introduction](#introduction)
2. [📂 Data Description](#data-description)
3. [🔍 Methodology](#methodology)
4. [✨ Results](#results)
5. [🖼 Visualization](#visualization)
6. [🔚 Conclusion](#conclusion)
7. [🚀 Running the Code](#running-the-code)

---

### 🌟 Introduction

Dive into the world of product reviews! By applying hierarchical clustering to these reviews, we aim to decode patterns and rhythms in customer feedback, painting a clearer picture of what users truly feel.

---

### 📂 Data Description

Peek into the dataset's core:

- **Product ID**: 🏷 Identifier for each unique product.
- **Title**: 📜 The product's title.
- **User ID**: 👤 Unique identifier for reviewers.
- **Helpfulness**: 👍 A ratio indicating how helpful others found the review.
- **Score**: ⭐ The numerical score assigned to the product.
- **Time**: ⏰ When was the review penned down?
- **Review Text**: 📝 Dive deep into the thoughts of the reviewer.
- **Category 1-3**: 📚 Hierarchical labels classifying the product.

---

### 🔍 Methodology

Our approach, step-by-step:

1. **Data Preprocessing**:
   - 🕵️‍♂️ Discover and handle the missing pieces.
   - 🔄 Normalize to understand the data on common ground.
   
2. **Hierarchical Clustering**:
   - 🧬 Use Ward's method for the linkage matrix.
   - 🌳 Visualize with a dendrogram.
   - ✂️ Cut and form distinct clusters.

3. **Cluster Analysis**:
   - 📊 Dive into each cluster's persona.

---

### ✨ Results

Clusters galore! Each cluster unveils a story, a pattern, binding similar reviews in a group. It's not just about scores; it's about when these scores echoed in the digital realm.

---

### 🖼 Visualization

🎨 A picture is worth a thousand words:

![image](https://github.com/DhruvSTrivedi/Hierarchical-Clustering-Analysis-on-Product-Reviews/assets/143839140/2032bda0-dca5-4f9f-bc17-0906cccb4f3e)



![image](https://github.com/DhruvSTrivedi/Hierarchical-Clustering-Analysis-on-Product-Reviews/assets/143839140/4134a859-63f6-4f2a-8432-0d2865372c2c)



---

### 🔚 Conclusion
---

**Business-Centric Conclusion**

In the dynamic world of product-based businesses, understanding customer feedback is paramount. Through our analysis, we delved deep into product reviews using hierarchical clustering, and the findings hold significant implications for business leaders and marketers.

**Feedback Over Time**:
The clustering process segmented reviews primarily based on the `Time` attribute. This means that at different periods, customers had distinct feedback patterns. Such temporal feedback shifts might be tied to:
- Product launches or updates
- Marketing campaigns
- Seasonal trends
- Competitor actions or market shifts

By identifying these time clusters, businesses can trace back to specific events or actions that led to particular feedback patterns.

**Consistent High Scores**:
The general trend of high scores across reviews indicates a positive customer reception. This is a testament to product quality or effective marketing. However, it also suggests a need for a more diverse feedback mechanism to capture nuanced opinions.

**Practical Implications for Businesses**:
1. **Targeted Marketing**: By understanding the periods when certain feedback patterns emerge, marketing teams can fine-tune their campaigns to address specific customer sentiments.
   
2. **Product Development**: Insights from specific time clusters can guide product teams in enhancing features or addressing issues. For instance, if a particular time cluster after a product update had varied feedback, the product team can delve into specifics and make informed iterations.
   
3. **Customer Support and Engagement**: Knowing when and how feedback trends shift allows customer support to prepare and engage proactively. For instance, during periods of mixed reviews, support can ramp up efforts to address concerns.

4. **Strategic Planning**: For business strategists, understanding these clusters means better forecasting. If certain periods consistently show specific feedback trends, strategies can be devised accordingly, be it for sales, marketing, or product launches.

**In Essence**:
This hierarchical clustering analysis isn't just about data; it's a compass pointing towards informed decision-making. For business leaders, it offers a structured view of customer feedback, transforming raw reviews into actionable insights. In a marketplace where understanding the voice of the customer can be the difference between growth and stagnation, such analyses are invaluable.

---

### 🚀 Running the Code

Get started:
1. Enter the portal:
   ```
   cd path-to-your-directory
   ```
2. Let the scripts run wild:
   ```
   python main.py
   ```

---
