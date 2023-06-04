import os
from pylive import LiveAPI

live = LiveAPI()

def convert_audio_to_midi():
    tracks = live.get_tracks()
    for track in tracks:
        clips = track.get_clips()
        for clip in clips:
            if clip.is_audio_clip():
                clip_name = clip.get_name()
                track_index = track.get_index()
                clip.start_playing()
                live.song().capture_midi(track_index, clip_name)

def extract_midi():
    tracks = live.get_tracks()
    for track in tracks:
        clips = track.get_clips()
        for clip in clips:
            if clip.is_midi_clip():
                clip_name = clip.get_name()
                track_index = track.get_index()
                clip.export_midi(track_index, clip_name)

def process_projects(folder_path):
    projects = os.listdir(folder_path)
    for project_file in projects:
        if project_file.endswith(".als"):
            project_path = os.path.join(folder_path, project_file)
            live.open_project(project_path)
            convert_audio_to_midi()
            extract_midi()
            live.close_project()

process_projects("Path/To/Projects/Folder")
