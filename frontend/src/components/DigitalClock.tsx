import React, { useState, useEffect } from "react";
import { Box, Text, HStack } from "@chakra-ui/react";

const DigitalClock: React.FC = () => {
    const [currentTime, setCurrentTime] = useState(new Date());

    useEffect(() => {
        const timer = setInterval(() => {
            setCurrentTime(new Date());
        }, 1000);

        return () => clearInterval(timer);
    }, []);

    const formatTime = (date: Date) => {
        return date.toLocaleTimeString("ko-KR", {
            hour12: false,
            hour: "2-digit",
            minute: "2-digit",
            second: "2-digit",
        });
    };

    const formatDate = (date: Date) => {
        return date.toLocaleDateString("ko-KR", {
            year: "numeric",
            month: "long",
            day: "numeric",
            weekday: "long",
        });
    };

    return (
        <Box textAlign="center" borderRadius="lg" borderColor="gray.200" mb={1}>
            <HStack spacing={4} justify="center">
                <Text fontSize="lg" color="gray.600">
                    {formatDate(currentTime)}
                </Text>
                <Text fontSize="2xl" fontWeight="bold" color="brand.600" fontFamily="monospace">
                    {formatTime(currentTime)}
                </Text>
            </HStack>
        </Box>
    );
};

export default DigitalClock;
