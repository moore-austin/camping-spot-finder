"""
// Interface Definition
// Owner: Designer
// Module: camping-spot-finder

Notice: The CampingSpotFinderInterface is only representative of the CampingSpotFinder 
implementation and should not be used directly. Please instantiate and use 
CampingSpotFinder with these exact methods unless otherwise stated.

Interface Details:
This module handles the discovery, evaluation, and physical disk storage of 
camping locations based on a strict weighting matrix. It uses general-purpose 
interfaces and defines errors out of existence via strict Pydantic schemas.
"""

from abc import ABC, abstractmethod
from pydantic import BaseModel, Field, HttpUrl
from typing import List

# ---------------------------------------------------------------------------
# Core Domain Entities (Defining Errors Out of Existence)
# ---------------------------------------------------------------------------

class GPSCoordinate(BaseModel):
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)

class BoundingBox(BaseModel):
    min_coord: GPSCoordinate
    max_coord: GPSCoordinate
    target_area: str = Field(..., description="e.g., 'Yellowstone_National_Park'")
    anchor_name: str = Field(..., description="e.g., 'North_Entrance_Cluster'")

class SiteRatings(BaseModel):
    """Raw 1-7 ratings for a given site."""
    cost: int = Field(..., ge=1, le=7)
    water_closeness: int = Field(..., ge=1, le=7)
    beauty: int = Field(..., ge=1, le=7)
    location_closeness: int = Field(..., ge=1, le=7)
    privacy: int = Field(..., ge=1, le=7)
    number_of_spots: int = Field(..., ge=1, le=7)
    openness: int = Field(..., ge=1, le=7)
    bear_risk: int = Field(..., ge=1, le=7)
    connectivity: int = Field(..., ge=1, le=7)
    road_accessibility: int = Field(..., ge=1, le=7)

class EvaluatedSite(BaseModel):
    """The final, computed data structure for a single campsite."""
    site_id: str
    site_name: str
    jurisdiction: str = Field(..., description="e.g., USFS, BLM, National Park")
    coordinates: GPSCoordinate
    raw_ratings: SiteRatings
    weighted_total: float
    summary: str
    reference_links: List[HttpUrl] = Field(
        default_factory=list, 
        description="List of verification URLs (e.g., iOverlander, Campendium, Recreation.gov)"
    )

class GeoCluster(BaseModel):
    """A collection of evaluated sites within a 5-mile driving radius."""
    target_area: str
    cluster_name: str
    anchor_coordinates: GPSCoordinate
    sites: List[EvaluatedSite]

# ---------------------------------------------------------------------------
# Service Interface
# ---------------------------------------------------------------------------

class CampingSpotFinderInterface(ABC):
    
    @abstractmethod
    def generate_cluster_boundary(self, anchor: GPSCoordinate, target_area: str, anchor_name: str) -> BoundingBox:
        """
        Creates a strict GPS bounding box representing a 5-mile driving radius 
        around the anchor coordinate within the specified target area.
        """
        pass

    @abstractmethod
    def discover_and_evaluate_sites(self, boundary: BoundingBox) -> GeoCluster:
        """
        Scouts locations within the BoundingBox, applies the 1-7 scoring matrix 
        with the defined multipliers, compiles reference links, and returns a 
        ranked GeoCluster.
        """
        pass

    @abstractmethod
    def persist_cluster_to_disk(self, cluster: GeoCluster) -> str:
        """
        Takes a computed GeoCluster and writes it to the local filesystem.
        Creates the directory `src/spots/[target_area]/[cluster_name]/` and 
        populates it with individual `[site_id].yaml` files.
        
        Returns:
            str: The physical directory path where the files were saved.
        """
        pass