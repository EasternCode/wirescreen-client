"""WireScreen.AI API Client"""
import os
from typing import Any, Dict, List, Optional
from urllib.parse import ParseResult, urljoin, urlparse
from uuid import UUID

import requests
import validators


SEARCH = "search"
DATA = "data"
SEARCH_PATH = "/".join([SEARCH, "search"])
ADVANCED_SEARCH_PATH = "/".join([SEARCH, "advancedsearch"])
ORGANIZATION_PATH = "/".join([DATA, "organization"])
ORGANIZATIONS_PATH = "/".join([DATA, "organizations"])
PERSON_PATH = "/".join([DATA, "person"])
PERSONS_PATH = "/".join([DATA, "persons"])


def _make_headers(token: str) -> Dict[str, str]:
    """Constructs valid WireScreen API headers with given token."""
    return {
        "Content-Type": "application/json",
        "Authorization": "Token {}".format(token),
    }


class WireScreenAPI:
    """Interface for data requests."""

    def __init__(self, host: str, token: Optional[str] = None) -> None:
        """Initialize"""
        if not host:
            raise Exception("No host was provided.")
        elif not validators.url(host):
            raise Exception("The host provided is not a valid URL.")
        self._host: ParseResult = urlparse(host)
        self._token: str = token or os.environ.get("WIRESCREEN_API_TOKEN")
        if not self._token:
            raise NameError("No WireScreen API token provided.")
        self._headers: Dict[str, str] = _make_headers(self._token)

    def search(self, query: str, num_results: Optional[int] = None) -> Dict[str, Any]:
        """Search for companies and people."""
        request_data = {
            "query": query,
            "num_results": num_results,
        }
        url = urljoin(self._host.geturl(), SEARCH_PATH)
        response = requests.get(url, headers=self._headers, params=request_data)
        response.raise_for_status()
        return response.json()

    def advanced_search(
        self,
        query: str,
        num_results: Optional[int] = None,
        limit_to_public: Optional[bool] = None,
        limit_to_government: Optional[bool] = None,
        limit_to_operating: Optional[bool] = None,
        region: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Advanced search for companies."""
        request_data = {
            "query": query,
            "num_results": num_results,
            "limit_to_public": limit_to_public,
            "limit_to_government": limit_to_government,
            "limit_to_operating": limit_to_operating,
            "region": region,
        }
        url = urljoin(self._host.geturl(), ADVANCED_SEARCH_PATH)
        response = requests.post(url, headers=self._headers, json=request_data)
        response.raise_for_status()
        return response.json()

    def get_organization(self, uid: UUID) -> Dict[str, Any]:
        """Retrieves data for the organization indicated by it's `uid`."""
        request_data = {"uid": str(uid)}
        url = urljoin(self._host.geturl(), ORGANIZATION_PATH)
        response = requests.get(url, headers=self._headers, params=request_data)
        response.raise_for_status()
        return response.json()

    def get_organizations(self, uuid_list: List[UUID]) -> Dict[str, Any]:
        """Retrieves data about multiple organizations indicated by their `uids`."""
        request_data = {"uuid_list": [str(uuid) for uuid in uuid_list]}
        url = urljoin(self._host.geturl(), ORGANIZATIONS_PATH)
        response = requests.post(url, headers=self._headers, json=request_data)
        response.raise_for_status()
        return response.json()

    def get_person(self, uid: UUID) -> Dict[str, Any]:
        """Retrieves data for the person indicated by it's `uid`."""
        request_data = {"uid": str(uid)}
        url = urljoin(self._host.geturl(), PERSON_PATH)
        response = requests.get(url, headers=self._headers, params=request_data)
        response.raise_for_status()
        return response.json()

    def get_persons(self, uuid_list: List[UUID]) -> Dict[str, Any]:
        """Retrieves data about multiple persons indicated by their `uids`."""
        request_data = {"uuid_list": [str(uuid) for uuid in uuid_list]}
        url = urljoin(self._host.geturl(), PERSONS_PATH)
        response = requests.post(url, headers=self._headers, json=request_data)
        response.raise_for_status()
        return response.json()
