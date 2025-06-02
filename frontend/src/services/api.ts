import axios from "axios";
import { Event, Cheering, Bachelor } from "../types";

const API_BASE_URL = "/api";

const api = axios.create({
    baseURL: API_BASE_URL,
});

export const apiService = {
    // Cheering
    getRandomCheering: async (): Promise<Cheering> => {
        const response = await api.get("/cheering/random");
        return response.data;
    },

    // Bachelor
    getBachelors: async (): Promise<Bachelor[]> => {
        const response = await api.get("/bachelors/");
        return response.data;
    },

    // Events
    getEvents: async (): Promise<Event[]> => {
        const response = await api.get("/events/");
        return response.data;
    },

    // Manual Crawling
    manualCrawl: async (): Promise<{ message: string }> => {
        const response = await api.post("/crawl/manual");
        return response.data;
    },
};
