import React, { useState, useEffect } from "react";
import { Box, Text, useToast } from "@chakra-ui/react";
import { apiService } from "../services/api";
import { Cheering } from "../types";

const CheeringMessage: React.FC = () => {
    const [cheering, setCheering] = useState<Cheering | null>(null);
    const [loading, setLoading] = useState(true);
    const toast = useToast();

    const fetchCheering = async () => {
        try {
            setLoading(true);
            const data = await apiService.getRandomCheering();
            setCheering(data);
        } catch (error) {
            toast({
                title: "응원 메시지를 불러올 수 없습니다",
                status: "error",
                duration: 3000,
                isClosable: true,
            });
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchCheering();
    }, []);

    return (
        <Box textAlign="center" mb={3} mx={6} borderRadius="xl" color="black" bg="green.400" p={2}>
            <Text fontSize="3xl" fontWeight="bold" display="flex" alignItems="center" justifyContent="center">
                {loading ? "..." : cheering?.cheer_message}
            </Text>
        </Box>
    );
};

export default CheeringMessage;
