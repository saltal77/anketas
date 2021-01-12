# -*- coding: utf-8 -*-

from survey.views.confirm_view import ConfirmView, FoundView, SearchView , my_handler404
from survey.views.index_view import IndexView
from survey.views.survey_completed import SurveyCompleted
from survey.views.survey_detail import SurveyDetail

__all__ = ["SurveyCompleted", "IndexView", "ConfirmView", "SurveyDetail", "FoundView", "SearchView", "my_handler404"]
