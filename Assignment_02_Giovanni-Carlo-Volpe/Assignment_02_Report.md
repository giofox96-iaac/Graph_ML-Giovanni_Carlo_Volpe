# Assignment 2: Graph Analysis of Architectural Structure
## Case Study: Uffizi Gallery, Florence (First and Second Floors)

### 1. Introduction and Choice of Subject
This report details a graph-based analysis of the architectural structure of the Uffizi Gallery in Florence, specifically focusing on its **first and second floors**. These floors were selected for this study because it is the heart of the Uffizi, housing the most historically significant and renowned artworks of the Italian Renaissance (including masterpieces by Botticelli, Leonardo da Vinci, Michelangelo, and Raphael). 

The architectural layout of the Uffizi—a classical U-shaped administrative building converted into a sequence of enfilade rooms connected by long, dominating corridors—provides a fascinating topology for spatial analysis. By translating its geometric features into a spatial graph, I can move beyond mere architectural intuition, enabling a precise, quantitative evaluation of how spaces are connected, accessed, and experienced by visitors.

<table style="width:100%; border: none;">
  <tr>
    <td style="text-align: center; border: none; width: 50%;">
      <img src="Visuals/6.%20visualize.png" alt="First Floor" width="100%" />
      <br><em>First Floor</em>
    </td>
    <td style="text-align: center; border: none; width: 50%;">
      <img src="Visuals/Second_floor/6.2%20visualize.png" alt="Second Floor" width="100%" />
      <br><em>Second Floor</em>
    </td>
  </tr>
</table>
<div style="text-align: center; margin-top: 10px;">
  <em>Figure 1: Cleaned and processed floor plans of the Uffizi Gallery.</em>
</div>

---

### 2. Analytical Framework and Spatial Intelligence
Following the methodology discussed in the module, the analysis was broken down into a series of quantitative measurements. By converting the floor plan into a topological grid and subsequently into an analysis graph, I can evaluate the building's performance in terms of movement and accessibility.

<table style="width:100%; border: none;">
  <tr>
    <td style="text-align: center; border: none; width: 50%;">
      <img src="Visuals/8.%20geometry%20and%20grid.png" alt="First Floor" width="100%" />
      <br><em>First Floor</em>
    </td>
    <td style="text-align: center; border: none; width: 50%;">
      <img src="Visuals/Second_floor/8.2%20geometry%20and%20grid.png" alt="Second Floor" width="100%" />
      <br><em>Second Floor</em>
    </td>
  </tr>
</table>
<div style="text-align: center; margin-top: 10px;">
  <em>Figure 2: Grid generation used to slice the floor plans.</em>
</div>

#### 2.1 Global Metrics: Closeness and Betweenness Centrality
To understand the underlying hierarchy of the gallery's spaces, foundational graph metrics were calculated:
*   **Closeness Centrality:** Measures how "integrated" a space is relative to the rest of the building. In the Uffizi, this helps identify the "center of gravity" of the layout—the spaces that require the least amount of walking to reach from all other rooms.

<table style="width:100%; border: none;">
  <tr>
    <td style="text-align: center; border: none; width: 50%;">
      <img src="Visuals/14.%20Closeness%20Centrality.png" alt="First Floor" width="100%" />
      <br><em>First Floor</em>
    </td>
    <td style="text-align: center; border: none; width: 50%;">
      <img src="Visuals/Second_floor/14.2%20closeness%20centrality.png" alt="Second Floor" width="100%" />
      <br><em>Second Floor</em>
    </td>
  </tr>
</table>
<div style="text-align: center; margin-top: 10px;">
  <em>Figure 3: Closeness Centrality mapping.</em>
</div>

*   **Betweenness Centrality:** This metric identifies "bridges" or "bottlenecks." Because the Uffizi has long corridors with single points of entry to specific wings, high betweenness values highlight critical flow corridors where the majority of visitor traffic inevitably converges. 

<table style="width:100%; border: none;">
  <tr>
    <td style="text-align: center; border: none; width: 50%;">
      <img src="Visuals/14.%20Betweenness%20Centrality.png" alt="First Floor" width="100%" />
      <br><em>First Floor</em>
    </td>
    <td style="text-align: center; border: none; width: 50%;">
      <img src="Visuals/Second_floor/14.2%20Betweenness%20Centrality.png" alt="Second Floor" width="100%" />
      <br><em>Second Floor</em>
    </td>
  </tr>
</table>
<div style="text-align: center; margin-top: 10px;">
  <em>Figure 4: Betweenness Centrality mapping.</em>
</div>

#### 2.2 Community Detection and Local Connectivity
A dense grid graph often obscures functional logic because every standard cell has an identical number of connections. To provide a functional reading of the building, **Community Partitioning** (using algorithms like Louvain) was applied.

By identifying dense clusters of nodes, the algorithm computationally recognizes individual rooms and functional zones from a unified floor plan surface. Once partitioned, I computed **Degree Centrality** on the resulting spatial clusters to determine local "connectivity". This successfully maps the "popularity" of rooms, distinguishing highly central gathering hubs from secluded, private exhibition fringes.

<table style="width:100%; border: none;">
  <tr>
    <td style="text-align: center; border: none; width: 50%;">
      <img src="Visuals/14.%20Community%20Detection.png" alt="First Floor" width="100%" />
      <br><em>First Floor</em>
    </td>
    <td style="text-align: center; border: none; width: 50%;">
      <img src="Visuals/Second_floor/14.2%20Community%20Detection.png" alt="Second Floor" width="100%" />
      <br><em>Second Floor</em>
    </td>
  </tr>
</table>
<div style="text-align: center; margin-top: 10px;">
  <em>Figure 5: Community Partitioning algorithm isolating functional zones.</em>
</div>

Following community detection, the communities are used to construct a consolidated model by generating a new boundary (or shell) that represents the distinct functional areas.

<table style="width:100%; border: none;">
  <tr>
    <td style="text-align: center; border: none; width: 50%;">
      <img src="Visuals/14.%20Degree%20centrality_New%20Shell.png" alt="First Floor" width="100%" />
      <br><em>First Floor</em>
    </td>
    <td style="text-align: center; border: none; width: 50%;">
      <img src="Visuals/Second_floor/14.2%20Degree%20centrality_New%20Shell.png" alt="Second Floor" width="100%" />
      <br><em>Second Floor</em>
    </td>
  </tr>
</table>
<div style="text-align: center; margin-top: 10px;">
  <em>Figure 6: The new shells generated from the community detection.</em>
</div>

From this new shell, a secondary macro-graph is extracted. This new graph represents the simplified topology of the functional zones (rooms), allowing me to analyze room-to-room connectivity rather than just grid cell connectivity.

<table style="width:100%; border: none;">
  <tr>
    <td style="text-align: center; border: none; width: 50%;">
      <img src="Visuals/14.%20Degree%20centrality_New%20Graph.png" alt="First Floor" width="100%" />
      <br><em>First Floor</em>
    </td>
    <td style="text-align: center; border: none; width: 50%;">
      <img src="Visuals/Second_floor/14.2%20Degree%20centrality_New%20Graph.png" alt="Second Floor" width="100%" />
      <br><em>Second Floor</em>
    </td>
  </tr>
</table>
<div style="text-align: center; margin-top: 10px;">
  <em>Figure 7: The new graphs extracted from the consolidated shells.</em>
</div>

<table style="width:100%; border: none;">
  <tr>
    <td style="text-align: center; border: none; width: 50%;">
      <img src="Visuals/14.%20Degree%20centrality_2_interpolated%20valuse.png" alt="First Floor" width="100%" />
      <br><em>First Floor</em>
    </td>
    <td style="text-align: center; border: none; width: 50%;">
      <img src="Visuals/Second_floor/14.2%20Degree%20centrality_2_interpolated%20valuse.png" alt="Second Floor" width="100%" />
      <br><em>Second Floor</em>
    </td>
  </tr>
</table>
<div style="text-align: center; margin-top: 10px;">
  <em>Figure 8: Degree Centrality interpolated over the floor logic.</em>
</div>

---

### 3. Targeted Routing: Shortest Path Analysis
One of the most practical applications of this graph analysis was computing the **Shortest Path** across the museum. 

In a museum as massive and dense as the Uffizi, visitors rarely have the time or energy to view every single piece. A highly common scenario involves a visitor arriving with an itinerary of specific, unmissable artworks (e.g., *The Birth of Venus*, the *Annunciation*). To simulate this, a series of specific Points of Interest (POIs) were plotted across the layout, representing targeted artwork locations.

Using the underlying navigation graph, the algorithm calculated the shortest, most efficient route sequence connecting these nodes. However, raw topological algorithms produce jagged, unnatural paths that snap strictly to grid centers. To resolve this, a `wire.straighten` method was employed. This method optimizes the jagged network segments into realistic, straight walking trajectories while strictly respecting the architectural boundaries (walls and inaccessible zones). 

<table style="width:100%; border: none;">
  <tr>
    <td style="text-align: center; border: none; width: 50%;">
      <img src="Visuals/14.%20shortest%20path%20between%20poi.png" alt="First Floor" width="100%" />
      <br><em>First Floor</em>
    </td>
    <td style="text-align: center; border: none; width: 50%;">
      <img src="Visuals/Second_floor/14.2%20shortest%20path%20between%20poi.png" alt="Second Floor" width="100%" />
      <br><em>Second Floor</em>
    </td>
  </tr>
</table>
<div style="text-align: center; margin-top: 10px;">
  <em>Figure 9: Straightened shortest paths connecting targeted Points of Interest.</em>
</div>

This analysis serves a dual purpose:
1.  **For the Visitor:** It mathematically minimizes walking distance when prioritizing specific rooms, preventing fatigue ("museum legs") and unnecessary backtracking in a complex environment.
2.  **For Facility Management:** By understanding the most efficient paths between star attractions, museum curators can anticipate crowd flows and potential congestion hotspots, optimizing wayfinding signage and security staff placement.

---

### 4. Conclusion
By transforming the Uffizi's 3D geometry into a mathematical graph, I extracted objective data on its spatial organization. The resulting metrics (Betweenness, Closeness, Degree Centrality) and pathfinding algorithms provide scientific precision to architectural analysis. Rather than guessing where congestion happens or how people might navigate between masterpieces, these computable frameworks unlock authentic "spatial intelligence," critical for managing flow and user experience in historic spaces.