import osmnx as ox
import networkx as nx
from geopy.distance import geodesic


G = ox.graph_from_point(
    (55.042135, 82.90138),
    dist=2000,
    network_type="walk"
)


def accessibility_weight(u, v, data, user_type="wheelchair"):

    length = data.get("length", 1)

    weight = length

    if data.get("highway") == "steps":
        if user_type == "wheelchair":
            weight += 2500
        elif user_type == "mobility":
            weight += 1200
        elif user_type == "sim":
            weight += 600
        else:
            weight += 2000

    if "incline" in data:
        try:
            incline = float(str(data["incline"]).replace("%", ""))
            if incline > 8:
                if user_type == "wheelchair":
                    weight += 800
                elif user_type == "mobility":
                    weight += 450
                elif user_type == "sim":
                    weight += 250
                else:
                    weight += 500
        except:
            pass

    return weight


def calculate_accessible_route(start_lat, start_lon, end_lat, end_lon, user_type="wheelchair"):

    orig = ox.distance.nearest_nodes(G, start_lon, start_lat)
    dest = ox.distance.nearest_nodes(G, end_lon, end_lat)

    route = nx.astar_path(
        G,
        orig,
        dest,
        heuristic=lambda u, v: 0,
        weight=lambda u, v, data: accessibility_weight(u, v, data, user_type)
    )


    route_coords = [(G.nodes[node]["y"], G.nodes[node]["x"]) for node in route]

    return route_coords
