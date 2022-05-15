import random
import streamlit as st
from streamlit.script_run_context import get_script_run_ctx
from streamlit.server.server import Server
from threading import Thread
from time import sleep

st.experimental_rerun()


def _get_session():
    session_id = get_report_ctx().session_id
    session_info = Server.get_current()._get_session_info()

    if session_info is None:
        raise RuntimeError("Couldn't get your Streamlit Session object.")

    return session_info.session


def _rerun_session(session, delay):
    sleep(delay)
    session.request_rerun()


def rerun(delay=0):
    session = _get_session()

    if delay <= 0:
        session.request_rerun()

    elif hasattr(session, "_rerun_thread") and session._rerun_thread.is_alive():
        return

    session._rerun_thread = Thread(target=_rerun_session, args=(session, delay))
    session._rerun_thread.start()