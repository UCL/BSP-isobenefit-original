import tkinter as tk

from src.simulation import run_isobenefit_simulation

args_types = {
    "urbanism_model": str,
    "size_x": int,
    "size_y": int,
    "n_steps": int,
    "max_population": int,
    "max_ab_km2": int,
    "build_probability": float,
    "neighboring_centrality_probability": float,
    "isolated_centrality_probability": float,
    "T_star": int,
    "random_seed": int,
    "density_factors": float,
    "prob_distribution": float,
}

string_inputs = [
    {"arg": "size_x", "name": "X size", "type": int, "default": 60},
    {"arg": "size_y", "name": "Y size", "type": int, "default": 60},
    {"arg": "n_steps", "name": "Iterartions", "type": int, "default": 20},
    {"arg": "max_population", "name": "Max Population", "type": int, "default": 100000},
    {"arg": "max_ab_km2", "name": "Max ab/km^2", "type": int, "default": 10000},
    {
        "arg": "build_probability",
        "name": "Build Block Probability",
        "type": float,
        "default": 0.3,
    },
    {
        "arg": "neighboring_centrality_probability",
        "name": "New Centrality P1",
        "type": float,
        "default": 0.1,
    },
    {
        "arg": "isolated_centrality_probability",
        "name": "New Centrality P2",
        "type": float,
        "default": 0,
    },
    {"arg": "T_star", "name": "T*", "type": int, "default": 5},
    {"arg": "random_seed", "name": "random seed", "type": int, "default": 42},
]


def make_interface(root, string_arguments_list):
    entries = {}
    entries["urbanism_model"] = make_radio_button(root)

    for field in string_arguments_list:
        print(field)
        row = tk.Frame(root)
        lab = tk.Label(row, width=22, text=field["name"] + ": ", anchor="w")
        ent = tk.Entry(row)
        ent.insert(0, field["default"])
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries[field["arg"]] = ent

    density_parameters = make_density_parameters_entries(root)
    entries.update(density_parameters)
    return entries


def make_radio_button(root):
    row = tk.Frame(root)
    urbanism_model = tk.StringVar(value="isobenefit")
    lab = tk.Label(row, width=22, text="City development model:", anchor="w")
    radio_buttons = tk.Frame(row)
    isobenefit_button = tk.Radiobutton(
        radio_buttons,
        text="isobenefit",
        variable=urbanism_model,
        indicatoron=0,
        value="isobenefit",
        width=12,
    )
    classical_button = tk.Radiobutton(
        radio_buttons,
        text="classical",
        variable=urbanism_model,
        indicatoron=0,
        value="classical",
        width=12,
    )
    isobenefit_button.pack(side="left")
    classical_button.pack(side="right")
    radio_buttons.pack(side="right")
    row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
    lab.pack(side=tk.LEFT)
    return urbanism_model


def make_density_parameters_entries(root):
    row = tk.Frame(root)
    tk.Label(row, text="Probability").grid(row=0, column=1)
    tk.Label(row, text="Dens. factor").grid(row=0, column=2)
    tk.Label(row, text="High").grid(row=1, column=0)
    tk.Label(row, text="Medium").grid(row=2, column=0)
    tk.Label(row, text="Low").grid(row=3, column=0)

    high_prob = tk.Entry(row)
    medium_prob = tk.Entry(row)
    low_prob = tk.Entry(row)

    high_prob.insert(0, 0.7)
    medium_prob.insert(0, 0.3)
    low_prob.insert(0, 0.0)

    high_factor = tk.Entry(row)
    medium_factor = tk.Entry(row)
    low_factor = tk.Entry(row)

    high_factor.insert(0, 1)
    medium_factor.insert(0, 0.1)
    low_factor.insert(0, 0.01)

    high_prob.grid(row=1, column=1)
    medium_prob.grid(row=2, column=1)
    low_prob.grid(row=3, column=1)

    high_factor.grid(row=1, column=2)
    medium_factor.grid(row=2, column=2)
    low_factor.grid(row=3, column=2)

    row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
    density_paramenters = {
        "prob_distribution": {
            "high_prob": high_prob,
            "medium_prob": medium_prob,
            "low_prob": low_prob,
        },
        "density_factors": {
            "high_factor": high_factor,
            "medium_factor": medium_factor,
            "low_factor": low_factor,
        },
    }
    return density_paramenters


def simluation_wrapper(entries, arguments_types):
    input_args = {}
    print(entries)
    for entry_name, entry_widget in entries.items():
        print(entry_name)
        _dtype = arguments_types[entry_name]
        if entry_name == "prob_distribution":
            print(entry_widget)
            input_args["prob_distribution"] = (
                _dtype(entry_widget["high_prob"].get()),
                _dtype(entry_widget["medium_prob"].get()),
                _dtype(entry_widget["low_prob"].get()),
            )
        elif entry_name == "density_factors":
            input_args["density_factors"] = (
                _dtype(entry_widget["high_factor"].get()),
                _dtype(entry_widget["medium_factor"].get()),
                _dtype(entry_widget["low_factor"].get()),
            )
        else:
            input_args[entry_name] = _dtype(entry_widget.get())

    input_args.update(
        {
            "input_filepath": None,
            "initialization_mode": "list",
            "output_path_prefix": None,
        }
    )
    run_isobenefit_simulation(**input_args)


if __name__ == "__main__":
    root = tk.Tk()

    ents = make_interface(root, string_inputs)
    print(ents)
    run_button = tk.Button(
        root,
        text="Run simulation",
        command=(lambda e=ents: simluation_wrapper(e, args_types)),
    )
    run_button.pack(side=tk.LEFT, padx=5, pady=5)
    quit_button = tk.Button(root, text="Quit", command=root.quit)
    quit_button.pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()
