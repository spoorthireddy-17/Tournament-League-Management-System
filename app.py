
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
from src.services import (
    sport_service,
    tournament_service,
    team_service,
    player_service,
    match_service
)
# Session state to track if dashboard is shown
if "show_dashboard" not in st.session_state:
    st.session_state.show_dashboard = True

# Function to hide dashboard and show main app
def go_to_app():
    st.session_state.show_dashboard = False
    # 🌟 FIX: Force a rerun of the script to update the UI immediately
    st.rerun()
# ---------------- DASHBOARD PAGE (Styling Focused) ----------------
if st.session_state.show_dashboard:
    # Set page config for a better dashboard look
    st.set_page_config(page_title="Tournament/League Management - Dashboard", layout="wide")

    # --- Header Banner ---
    st.markdown(
        """
        <div style='
    background-color:#59AC77; /* Brighter Green */
    padding:40px; /* More Padding */
    border-radius:20px; /* More rounded */
    text-align:center;
    box-shadow:4px 4px 15px rgba(0,0,0,0.3); /* Stronger Shadow */
    width: 100%;
    margin: 0 auto;
'>
    <h1 style='font-size:55px; color:#ffffff; text-shadow: 1px 1px 2px #333;'>🏆 Tournament / League Management</h1>
    <p style='font-size:22px; color:#e0e0e0;'>Welcome! Get a snapshot of your sports data below before diving in.</p>
</div>

        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)
    
    ## 📊 System Overview

    # Fetch data for counts (Stubs for data fetching)
    try:
        total_sports = len(sport_service.SportService.list_sports())
    except Exception:
        total_sports = 0
    
    try:
        total_tournaments = len(tournament_service.TournamentService.list_tournaments())
    except Exception:
        total_tournaments = 0

    try:
        total_teams = len(team_service.TeamService.list_teams())
    except Exception:
        total_teams = 0

    try:
        total_players = len(player_service.PlayerService.list_players())
    except Exception:
        total_players = 0
        
    try:
        total_matches = len(match_service.MatchService.list_matches())
    except Exception:
        total_matches = 0

    st.markdown("## 📊 System Overview", unsafe_allow_html=True)
    st.markdown("---")

    # Custom metric cards for better styling
    col1, col2, col3, col4, col5 = st.columns(5)

    def colored_metric(col, label, value, color):
        col.markdown(f"""
            <div style="background-color:{color}; padding:20px; border-radius:10px; text-align:center; box-shadow:2px 2px 8px rgba(0,0,0,0.2); height: 120px;">
                <p style="font-size:16px; color:#ffffff; margin:0;">{label}</p>
                <h2 style="font-size:40px; color:#ffffff; margin:5px 0 0 0;">{value}</h2>
            </div>
        """, unsafe_allow_html=True)

    colored_metric(col1, "Total Sports", total_sports, "#FF6347") # Tomato
    colored_metric(col2, "Total Tournaments", total_tournaments, "#4682B4") # SteelBlue
    colored_metric(col3, "Total Teams", total_teams, "#FFD700") # Gold
    colored_metric(col4, "Total Players", total_players, "#3CB371") # MediumSeaGreen
    colored_metric(col5, "Total Matches", total_matches, "#8A2BE2") # BlueViolet


    st.markdown("<br><br>", unsafe_allow_html=True)
    
    ## 🗓️ Active Tournaments at a Glance

    st.markdown("## 🗓️ Active Tournaments at a Glance", unsafe_allow_html=True)
    st.markdown("---")
    
    tournaments = tournament_service.TournamentService.list_tournaments()
    if tournaments:
        df_tournaments = pd.DataFrame(tournaments)
        # Display only key columns
        df_display = df_tournaments[['tournament_id', 'name', 'type', 'start_date', 'end_date']].rename(
            columns={'tournament_id': 'ID', 'name': 'Name', 'type': 'Type', 'start_date': 'Start', 'end_date': 'End'}
        )
        
        # Display with AgGrid for better interactive styling (if desired, use basic dataframe if AGGrid is too heavy)
        st.dataframe(df_display, use_container_width=True, hide_index=True)
    else:
        st.info("No tournaments found. Enter the app to add one!")

    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- Enter App Button ---
    col_a, col_b, col_c = st.columns([1, 2, 1])
    with col_b:
        st.markdown("<h2 style='text-align: center; color:#1f3d3d;'>Ready to manage your league?</h2>", unsafe_allow_html=True)
        # Using a custom button style
        st.markdown(
            """
            <style>
            div.stButton > button {
                background-color: #2E8B57; /* Sea Green */
                color: white;
                padding: 15px 30px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 20px;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 12px;
                border: none;
                box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
            }
            div.stButton > button:hover {
                background-color: #3CB371; /* Medium Sea Green on hover */
            }
            </style>
            """, unsafe_allow_html=True
        )
        if st.button("🚀 START MANAGING", key="enter_app_btn", use_container_width=True):
            go_to_app() # This now triggers the st.rerun()
else:
    # ---------------- MAIN APP ----------------
    # ---------------- MAIN APP (Minimalist & Neat Look) ----------------

    st.set_page_config(page_title="Tournament/League Management", layout="wide")

    # --- Inject Custom CSS for Neat Background, Fonts, and Tabs ---
    PRIMARY_COLOR = "#0078D4"  # A clean, professional blue
    ACCENT_COLOR = "#1f3d3d"   # Dark Forest Green/Teal

    st.markdown(
        f"""
        <style>
        /* 1. Overall Background and Fonts */
        .stApp {{
            background-color: #f8f9fa; /* Very light gray/near-white background */
            color: #343a40; /* Dark gray text */
            font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        }}
        
        /* 2. Main Title Styling */
        h1 {{
            color: {ACCENT_COLOR}; 
            font-size: 2.5em;
            font-weight: 600;
            border-bottom: 2px solid #e9ecef; /* Thin, light gray underline */
            padding-bottom: 15px;
            margin-bottom: 25px;
        }}

        /* 3. Tab Styling (Clean and Professional) */
        .stTabs [data-baseweb="tab-list"] {{
            gap: 1px; /* Minimal space between tabs */
            border-bottom: 1px solid #ced4da; /* Light gray line */
            margin-bottom: 0;
        }}

        .stTabs [data-baseweb="tab"] {{
            height: 45px;
            padding: 10px 20px;
            font-size: 1.05em;
            color: #6c757d; /* Muted text for unselected tab */
            background-color: #f0f2f5; /* Subtle background difference */
            border-radius: 6px 6px 0 0;
            margin-right: 5px;
            transition: all 0.2s ease-in-out;
        }}
        
        /* Hover Effect for Unselected Tabs */
        .stTabs [data-baseweb="tab"]:hover {{
            color: {PRIMARY_COLOR};
        }}

        .stTabs [aria-selected="true"] {{
            background-color: #ffffff; /* White background for the active pane */
            color: {PRIMARY_COLOR}; /* Primary blue text for active tab */
            border-top: 3px solid {PRIMARY_COLOR}; /* Blue line above the active tab */
            border-left: 1px solid #ced4da;
            border-right: 1px solid #ced4da;
            border-bottom: 1px solid #ffffff; /* Seamless transition to the pane */
            margin-bottom: -1px; /* Pull tab down to overlap bottom border */
            font-weight: bold;
        }}
        
        /* 4. Widget Enhancements (Buttons, Selectboxes) */
        .stButton button {{
            background-color: {PRIMARY_COLOR}; 
            color: white;
            border-radius: 4px;
            border: 1px solid {PRIMARY_COLOR};
            padding: 8px 15px;
            font-weight: 500;
            transition: background-color 0.2s;
        }}
        .stButton button:hover {{
            background-color: #005a9e; /* Darker blue on hover */
            border-color: #005a9e;
        }}

        /* 5. Header inside Tabs (Sport, Tournaments, etc.) */
        h2 {{
            color: {ACCENT_COLOR}; 
            font-size: 1.8em;
            border-left: 4px solid {PRIMARY_COLOR}; /* Blue vertical line */
            padding-left: 10px;
            margin-top: 25px;
            margin-bottom: 20px;
        }}
        
        /* 6. Subheader/Group Titles (Team, Tournament name) */
        h3 {{
            color: {PRIMARY_COLOR};
            font-size: 1.4em;
            border-bottom: 1px solid #f0f2f5;
            padding-bottom: 5px;
            margin-top: 20px;
        }}
        
        /* 7. AgGrid container styling */
        .ag-root-wrapper {{
            border-radius: 4px;
            border: 1px solid #e9ecef; /* Subtle border */
        }}
        
        /* 8. Warning/Info Messages */
        .stAlert {{
            border-radius: 4px;
        }}
        
        </style>
        """,
        unsafe_allow_html=True
    )
    # --- End Custom CSS Injection ---

    st.set_page_config(page_title="Tournament/League Management", layout="wide")
    st.title("🏆 Tournament / League Management System")

    tabs = st.tabs(["Sports", "Tournaments", "Teams", "Players", "Matches", "Standings"])

    def display_df_aggrid(df):
        if df.empty:
            st.warning("No data available")
        else:
            gb = GridOptionsBuilder.from_dataframe(df)
            gb.configure_side_bar()
            #gb.configure_pagination(paginationAutoPageSize=False, paginationPageSize=len(df))
            gridOptions = gb.build()
            AgGrid(df, gridOptions=gridOptions, enable_enterprise_modules=True, fit_columns_on_grid_load=True)


    # ------------------ SPORTS TAB ------------------
    with tabs[0]:
        st.header("Sports")
        action = st.selectbox(
            "Choose action",
            ["", "Add Sport", "View All Sports", "View Sport by ID", "Update Sport", "Delete Sport"],
            key="sports_action"
        )

        if action == "Add Sport":
            name = st.text_input("Sport Name", key="add_sport_name")
            players_required = st.number_input("Players Required", min_value=1, step=1, key="add_sport_players")
            if st.button("Add Sport", key="add_sport_btn"):
                sport_service.SportService.add_sport(name, players_required)
                st.success(f"Sport '{name}' added successfully!")

        elif action == "View All Sports":
            sports = sport_service.SportService.list_sports()
            display_df_aggrid(pd.DataFrame(sports))

        elif action == "View Sport by ID":
            sport_id = st.number_input("Sport ID", min_value=1, step=1, key="view_sport_id")
            if st.button("View Sport", key="view_sport_btn"):
                sport = sport_service.SportService.get_sport(sport_id)
                display_df_aggrid(pd.DataFrame([sport]) if sport else pd.DataFrame())

        elif action == "Update Sport":
            sport_id = st.number_input("Sport ID", min_value=1, step=1, key="update_sport_id")
            new_name = st.text_input("New Name", key="update_sport_name")
            new_players = st.number_input("Players Required", min_value=1, step=1, key="update_sport_players")
            if st.button("Update Sport", key="update_sport_btn"):
                sport_service.SportService.update_sport(sport_id, new_name, new_players)
                st.success("Sport updated successfully!")

        elif action == "Delete Sport":
            sport_id = st.number_input("Sport ID", min_value=1, step=1, key="delete_sport_id")
            if st.button("Delete Sport", key="delete_sport_btn"):
                sport_service.SportService.delete_sport(sport_id)
                st.success("Sport deleted successfully!")


    # ------------------ TOURNAMENTS TAB ------------------
    with tabs[1]:
        st.header("Tournaments")
        action = st.selectbox(
            "Choose action",
            ["", "Add Tournament", "View All Tournaments", "View Tournament by ID", "Update Tournament", "Delete Tournament"],
            key="tournament_action"
        )

        if action == "Add Tournament":
            name = st.text_input("Tournament Name", key="add_tournament_name")
            ttype = st.selectbox("Type", ["League", "Knockout"], key="add_tournament_type")
            start_date = st.date_input("Start Date", key="add_tournament_start")
            end_date = st.date_input("End Date", key="add_tournament_end")
            sport_id = st.number_input("Sport ID", min_value=1, step=1, key="add_tournament_sport")
            if st.button("Add Tournament", key="add_tournament_btn"):
                tournament_service.TournamentService.add_tournament(
                    name, ttype, start_date.isoformat(), end_date.isoformat(), sport_id
                )
                st.success(f"Tournament '{name}' added successfully!")

        elif action == "View All Tournaments":
            tournaments = tournament_service.TournamentService.list_tournaments()
            display_df_aggrid(pd.DataFrame(tournaments))

        elif action == "View Tournament by ID":
            tournament_id = st.number_input("Tournament ID", min_value=1, step=1, key="view_tournament_id")
            if st.button("View Tournament", key="view_tournament_btn"):
                tournament = tournament_service.TournamentService.get_tournament(tournament_id)
                display_df_aggrid(pd.DataFrame([tournament]) if tournament else pd.DataFrame())

        elif action == "Update Tournament":
            tournament_id = st.number_input("Tournament ID", min_value=1, step=1, key="update_tournament_id")
            new_name = st.text_input("New Name", key="update_tournament_name")
            new_type = st.selectbox("Type", ["League", "Knockout"], key="update_tournament_type")
            new_start = st.date_input("Start Date", key="update_tournament_start")
            new_end = st.date_input("End Date", key="update_tournament_end")
            new_sport = st.number_input("Sport ID", min_value=1, step=1, key="update_tournament_sport")
            if st.button("Update Tournament", key="update_tournament_btn"):
                tournament_service.TournamentService.update_tournament(
                    tournament_id, new_name, new_type, new_start.isoformat(), new_end.isoformat(), new_sport
                )
                st.success("Tournament updated successfully!")

        elif action == "Delete Tournament":
            tournament_id = st.number_input("Tournament ID", min_value=1, step=1, key="delete_tournament_id")
            if st.button("Delete Tournament", key="delete_tournament_btn"):
                tournament_service.TournamentService.delete_tournament(tournament_id)
                st.success("Tournament deleted successfully!")


    # ------------------ TEAMS TAB ------------------
    with tabs[2]:
        st.header("Teams")
        action = st.selectbox(
            "Choose action",
            ["", "Add Team", "View All Teams", "View Team by ID", "Update Team", "Delete Team"],
            key="team_action"
        )

        if action == "Add Team":
            name = st.text_input("Team Name", key="add_team_name")
            coach = st.text_input("Coach Name", key="add_team_coach")
            tournament_id = st.number_input("Tournament ID", min_value=1, step=1, key="add_team_tournament")
            if st.button("Add Team", key="add_team_btn"):
                team_service.TeamService.add_team(name, coach, tournament_id)
                st.success(f"Team '{name}' added successfully!")

        elif action == "View All Teams":
            teams = team_service.TeamService.list_teams()
            tournaments = tournament_service.TournamentService.list_tournaments()
            if teams:
                df = pd.DataFrame(teams)
                tournament_df = pd.DataFrame(tournaments)[['tournament_id', 'name']].rename(columns={'name': 'Tournament'})
                df = df.merge(tournament_df, on='tournament_id', how='left')
                grouped = df.groupby('Tournament')
                for tournament, group in grouped:
                    st.subheader(f"Tournament: {tournament}")
                    # Drop 'team_id', show team_name instead
                    display_df_aggrid(group.drop(columns=['Tournament', 'team_id']))
            else:
                st.warning("No teams found")


        elif action == "View Team by ID":
            team_id = st.number_input("Team ID", min_value=1, step=1, key="view_team_id")
            if st.button("View Team", key="view_team_btn"):
                team = team_service.TeamService.get_team(team_id)
                display_df_aggrid(pd.DataFrame([team]) if team else pd.DataFrame())

        elif action == "Update Team":
            team_id = st.number_input("Team ID", min_value=1, step=1, key="update_team_id")
            new_name = st.text_input("Team Name", key="update_team_name")
            new_coach = st.text_input("Coach Name", key="update_team_coach")
            new_tournament = st.number_input("Tournament ID", min_value=1, step=1, key="update_team_tournament")
            if st.button("Update Team", key="update_team_btn"):
                team_service.TeamService.update_team(team_id, new_name, new_coach, new_tournament)
                st.success("Team updated successfully!")

        elif action == "Delete Team":
            team_id = st.number_input("Team ID", min_value=1, step=1, key="delete_team_id")
            if st.button("Delete Team", key="delete_team_btn"):
                team_service.TeamService.delete_team(team_id)
                st.success("Team deleted successfully!")

    # ------------------ PLAYERS TAB (Grouped by Team) ------------------
    with tabs[3]:
        st.header("Players")
        action = st.selectbox(
            "Choose action",
            ["", "Add Player", "View All Players", "View Player by ID", "Update Player", "Delete Player"],
            key="player_action"
        )

        if action == "Add Player":
            name = st.text_input("Player Name", key="add_player_name")
            age = st.number_input("Age", min_value=1, step=1, key="add_player_age")
            position = st.text_input("Position", key="add_player_position")
            team_id = st.number_input("Team ID", min_value=1, step=1, key="add_player_team")
            if st.button("Add Player", key="add_player_btn"):
                player_service.PlayerService.add_player(name, age, position, team_id)
                st.success(f"Player '{name}' added successfully!")

        elif action == "View All Players":
            players = player_service.PlayerService.list_players()
            if not players:
                st.warning("No players found")
            else:
                df = pd.DataFrame(players)
                teams = team_service.TeamService.list_teams()
                team_df = pd.DataFrame(teams)
                df = df.merge(team_df[['team_id', 'team_name']], on='team_id', how='left')
                grouped = df.groupby('team_name')
                for team, group in grouped:
                    st.subheader(f"Team: {team}")
                    display_df_aggrid(group.drop(columns=['team_name']))

        elif action == "View Player by ID":
            player_id = st.number_input("Player ID", min_value=1, step=1, key="view_player_id")
            if st.button("View Player", key="view_player_btn"):
                player = player_service.PlayerService.get_player(player_id)
                display_df_aggrid(pd.DataFrame([player]) if player else pd.DataFrame())

        elif action == "Update Player":
            player_id = st.number_input("Player ID", min_value=1, step=1, key="update_player_id")
            new_name = st.text_input("Player Name", key="update_player_name")
            new_age = st.number_input("Age", min_value=1, step=1, key="update_player_age")
            new_pos = st.text_input("Position", key="update_player_position")
            new_team = st.number_input("Team ID", min_value=1, step=1, key="update_player_team")
            if st.button("Update Player", key="update_player_btn"):
                player_service.PlayerService.update_player(player_id, new_name, new_age, new_pos, new_team)
                st.success("Player updated successfully!")

        elif action == "Delete Player":
            player_id = st.number_input("Player ID", min_value=1, step=1, key="delete_player_id")
            if st.button("Delete Player", key="delete_player_btn"):
                player_service.PlayerService.delete_player(player_id)
                st.success("Player deleted successfully!")


    # ------------------ MATCHES TAB (Grouped by Tournament) ------------------
    with tabs[4]:
        st.header("Matches")
        action = st.selectbox(
            "Choose action",
            ["", "Add Match", "View All Matches", "View Match by ID", "Update Match", "Delete Match"],
            key="match_action"
        )

        if action == "Add Match":
            tournament_id = st.number_input("Tournament ID", min_value=1, step=1, key="add_match_tournament")
            team1_id = st.number_input("Team 1 ID", min_value=1, step=1, key="add_match_team1")
            team2_id = st.number_input("Team 2 ID", min_value=1, step=1, key="add_match_team2")
            score1 = st.number_input("Score Team 1", min_value=0, step=1, key="add_match_score1")
            score2 = st.number_input("Score Team 2", min_value=0, step=1, key="add_match_score2")
            winner_id = st.number_input("Winner Team ID (0 if draw)", min_value=0, step=1, key="add_match_winner")
            match_date = st.date_input("Match Date", key="add_match_date")
            if st.button("Add Match", key="add_match_btn"):
                match_service.MatchService.add_match(
                    tournament_id, team1_id, team2_id, score1, score2, winner_id, match_date.isoformat()
                )
                st.success("Match added successfully!")

        elif action == "View All Matches":
            matches = match_service.MatchService.list_matches()
            if not matches:
                st.warning("No matches found")
            else:
                df = pd.DataFrame(matches)

                # Get tournament names
                tournaments = tournament_service.TournamentService.list_tournaments()
                tournament_df = pd.DataFrame(tournaments)[['tournament_id', 'name']]
                df = df.merge(tournament_df, left_on='tournament_id', right_on='tournament_id', how='left')
                
                # Get team names
                teams = team_service.TeamService.list_teams()
                team_df = pd.DataFrame(teams)[['team_id', 'team_name']]
                
                # Merge team1 and team2 names
                df = df.merge(team_df, left_on='team1_id', right_on='team_id', how='left').rename(columns={'team_name': 'Team 1 Name'})
                df = df.merge(team_df, left_on='team2_id', right_on='team_id', how='left').rename(columns={'team_name': 'Team 2 Name'})
                
                # Format team columns as "Name (ID)"
                df['Team 1'] = df.apply(lambda x: f"{x['Team 1 Name']} ({x['team1_id']})", axis=1)
                df['Team 2'] = df.apply(lambda x: f"{x['Team 2 Name']} ({x['team2_id']})", axis=1)
                
                # Drop old columns
                df = df.drop(columns=['team1_id', 'team2_id', 'team_id_x', 'team_id_y', 'Team 1 Name', 'Team 2 Name'])
                
                # Group by tournament and display cards
                grouped = df.groupby('name')
                for tournament_name, group in grouped:
                    st.markdown(f"### 🏆 {tournament_name}")
                    for _, row in group.iterrows():
                        st.markdown(f"""
                        <div style='border:1px solid #ddd; padding:15px; margin:5px; border-radius:10px; background:#f9f9f9'>
                            <strong>{row['Team 1']} vs {row['Team 2']}</strong><br>
                            Score: {row['score_team1']} - {row['score_team2']}<br>
                            Winner: {row['winner']}<br>
                            Date: {row['match_date']}
                        </div>
                        """, unsafe_allow_html=True)


        elif action == "View Match by ID":
            tournament_id = st.number_input("Tournament ID", min_value=1, step=1, key="view_match_tournament_id")
            if st.button("View Matches", key="view_matches_btn"):
                # Get all matches
                matches = match_service.MatchService.list_matches()
                # Filter by tournament
                matches = [m for m in matches if m['tournament_id'] == tournament_id]

                if not matches:
                    st.warning("No matches found for this tournament")
                else:
                    # Get team names
                    teams = team_service.TeamService.list_teams()
                    team_df = pd.DataFrame(teams)[['team_id', 'team_name']]
                    
                    for match in matches:
                        # Get team names
                        team1_name = team_df[team_df['team_id'] == match['team1_id']]['team_name'].values[0]
                        team2_name = team_df[team_df['team_id'] == match['team2_id']]['team_name'].values[0]

                        # Display match as a card
                        st.markdown(
                            f"""
                            <div style="background-color:#f0f0f0; padding:15px; margin:10px 0; border-radius:10px; box-shadow:2px 2px 5px rgba(0,0,0,0.1);">
                                <h4>Match ID: {match['match_id']}</h4>
                                <p><strong>Team 1:</strong> {team1_name} ({match['team1_id']})</p>
                                <p><strong>Team 2:</strong> {team2_name} ({match['team2_id']})</p>
                            <p><strong>Score:</strong> {match.get('score_team1', 0)} - {match.get('score_team2', 0)}</p>
                                <p><strong>Winner:</strong> {match.get('winner', 'TBD')}</p>
                                <p><strong>Date:</strong> {match.get('match_date', 'TBD')}</p>
                            </div>
                            """, unsafe_allow_html=True
                        )



        elif action == "Update Match":
            match_id = st.number_input("Match ID", min_value=1, step=1, key="update_match_id")
            tournament_id = st.number_input("Tournament ID", min_value=1, step=1, key="update_match_tournament")
            team1_id = st.number_input("Team 1 ID", min_value=1, step=1, key="update_match_team1")
            team2_id = st.number_input("Team 2 ID", min_value=1, step=1, key="update_match_team2")
            score1 = st.number_input("Score Team 1", min_value=0, step=1, key="update_match_score1")
            score2 = st.number_input("Score Team 2", min_value=0, step=1, key="update_match_score2")
            winner_id = st.number_input("Winner Team ID (0 if draw)", min_value=0, step=1, key="update_match_winner")
            match_date = st.date_input("Match Date", key="update_match_date")
            if st.button("Update Match", key="update_match_btn"):
                match_service.MatchService.update_match(
                    match_id, tournament_id, team1_id, team2_id, score1, score2, winner_id, match_date.isoformat()
                )
                st.success("Match updated successfully!")

        elif action == "Delete Match":
            match_id = st.number_input("Match ID", min_value=1, step=1, key="delete_match_id")
            if st.button("Delete Match", key="delete_match_btn"):
                match_service.MatchService.delete_match(match_id)
                st.success("Match deleted successfully!")

    # ------------------ STANDINGS TAB ------------------
    with tabs[5]:
        st.header("Standings")

        # Select tournament
        tournament_id = st.number_input(
            "Tournament ID", min_value=1, step=1, key="standings_tournament_id"
        )

        # Get all matches for this tournament
        matches = match_service.MatchService.list_matches()
        tournament_matches = [m for m in matches if m['tournament_id'] == tournament_id]

        if not tournament_matches:
            st.info("No matches played for this tournament yet.")
        else:
            from collections import defaultdict

            # Compute standings
            standings = defaultdict(lambda: {
                "matches_played": 0,
                "wins": 0,
                "losses": 0,
                "draws": 0,
                "points": 0
            })

            for match in tournament_matches:
                team1 = match['team1_id']
                team2 = match['team2_id']
                winner = match.get('winner', 0)  # <-- corrected key

                # Matches played
                standings[team1]['matches_played'] += 1
                standings[team2]['matches_played'] += 1

                # Wins, Losses, Draws, Points
                if winner == 0:  # Draw
                    standings[team1]['draws'] += 1
                    standings[team2]['draws'] += 1
                    standings[team1]['points'] += 1
                    standings[team2]['points'] += 1
                else:
                    standings[winner]['wins'] += 1
                    standings[winner]['points'] += 3
                    loser = team2 if winner == team1 else team1
                    standings[loser]['losses'] += 1

            # Convert to DataFrame
            teams = team_service.TeamService.list_teams()
            team_map = {t['team_id']: t['team_name'] for t in teams}

            data = []
            for team_id, stats in standings.items():
                data.append({
                    "Team": f"{team_map.get(team_id, 'Unknown')} ({team_id})",
                    **stats
                })

            df = pd.DataFrame(data)

            # Sort by points, then wins
            df = df.sort_values(by=["points", "wins"], ascending=[False, False]).reset_index(drop=True)

            # Add Rank column
            df.insert(0, "Rank", df.index + 1)

            # Display standings
            display_df_aggrid(df)
