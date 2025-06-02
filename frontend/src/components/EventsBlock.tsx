import React, { useState, useEffect } from "react";
import { Box, Text, VStack, Spinner, Alert, AlertIcon, Link } from "@chakra-ui/react";
import { apiService } from "../services/api";
import { Event } from "../types";

const EventsBlock: React.FC = () => {
    const [events, setEvents] = useState<Event[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchEvents = async () => {
            try {
                setLoading(true);
                const data = await apiService.getEvents();
                setEvents(data);
                setError(null);
            } catch (err) {
                setError("이벤트 데이터를 불러올 수 없습니다");
            } finally {
                setLoading(false);
            }
        };

        fetchEvents();
    }, []);

    if (loading) {
        return (
            <Box p={6} textAlign="center">
                <Spinner size="lg" color="brand.500" />
                <Text mt={4}>이벤트 로딩 중...</Text>
            </Box>
        );
    }

    if (error) {
        return (
            <Alert status="error">
                <AlertIcon />
                {error}
            </Alert>
        );
    }

    return (
        <Box bg="white" borderRadius="lg" shadow="md" p={6} h="600px" overflowY="auto">
            <Text fontSize="lg" fontWeight="bold" mb={4} color="brand.600">
                📅 행사
            </Text>
            <VStack spacing={3} align="stretch">
                {events.length === 0 ? (
                    <Text color="gray.500" textAlign="center">
                        등록된 이벤트가 없습니다
                    </Text>
                ) : (
                    events.map((event) =>
                        event.evt_url ? (
                            <Link
                                key={event.evt_id}
                                href={event.evt_url}
                                isExternal
                                _hover={{ textDecoration: "none" }}
                            >
                                <Box
                                    p={5}
                                    bg="white"
                                    borderRadius="xl"
                                    border="1px"
                                    borderColor="gray.100"
                                    shadow="sm"
                                    cursor="pointer"
                                    transition="all 0.2s ease"
                                    _hover={{
                                        shadow: "lg",
                                        transform: "translateY(-2px)",
                                        borderColor: "brand.200",
                                        bg: "gray.50",
                                    }}
                                >
                                    <Box display="flex" justifyContent="space-between" alignItems="flex-start" mb={2}>
                                        <Text
                                            fontWeight="600"
                                            fontSize="sm"
                                            color="gray.800"
                                            lineHeight="1.4"
                                            flex="1"
                                            mr={2}
                                        >
                                            {event.evt_title}
                                        </Text>
                                    </Box>
                                    <Text fontSize="xs" color="gray.500" fontWeight="500">
                                        {event.evt_date}
                                    </Text>
                                </Box>
                            </Link>
                        ) : (
                            <Box
                                key={event.evt_id}
                                p={5}
                                bg="white"
                                borderRadius="xl"
                                border="1px"
                                borderColor="gray.100"
                                shadow="sm"
                                transition="all 0.2s ease"
                            >
                                <Box display="flex" justifyContent="space-between" alignItems="flex-start" mb={2}>
                                    <Text
                                        fontWeight="600"
                                        fontSize="md"
                                        color="gray.800"
                                        lineHeight="1.4"
                                        flex="1"
                                        mr={2}
                                    >
                                        {event.evt_title}
                                    </Text>
                                </Box>
                                <Text fontSize="sm" color="gray.500" fontWeight="500">
                                    {event.evt_date}
                                </Text>
                            </Box>
                        )
                    )
                )}
            </VStack>
        </Box>
    );
};

export default EventsBlock;
