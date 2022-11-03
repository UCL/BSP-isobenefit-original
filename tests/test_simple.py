from src.simulation import run_isobenefit_simulation

run_isobenefit_simulation(
    size_x=100,
    size_y=100,
    n_steps=20,
    output_path_prefix="test",
    build_probability=0.5,
    neighboring_centrality_probability=5e-3,
    isolated_centrality_probability=1e-1,
    T_star=10,
    random_seed=42,
    input_filepath=None,
    initialization_mode="list",
    max_population=1000000,
    max_ab_km2=10000,
    urbanism_model="isobenefit",
    prob_distribution=(0.7, 0.3, 0),
    density_factors=(1, 0.1, 0.01),
)
