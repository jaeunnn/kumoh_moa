import React, { useState } from "react";
import { Button, useToast } from "@chakra-ui/react";
import { apiService } from "../services/api";

const CrawlingButton: React.FC = () => {
    const [loading, setLoading] = useState(false);
    const toast = useToast();

    const handleCrawl = async () => {
        try {
            setLoading(true);
            await apiService.manualCrawl();
            toast({
                title: "크롤링 완료",
                description: "데이터가 성공적으로 업데이트되었습니다",
                status: "success",
                duration: 3000,
                isClosable: true,
            });
            // 페이지 새로고침으로 데이터 갱신
            window.location.reload();
        } catch (error) {
            toast({
                title: "크롤링 실패",
                description: "크롤링 중 오류가 발생했습니다",
                status: "error",
                duration: 3000,
                isClosable: true,
            });
        } finally {
            setLoading(false);
        }
    };

    return (
        <Button
            position="fixed"
            bottom="20px"
            right="20px"
            colorScheme="brand"
            size="sm"
            onClick={handleCrawl}
            isLoading={loading}
            loadingText="크롤링중"
            zIndex={1000}
            shadow="lg"
        >
            수동 크롤링
        </Button>
    );
};

export default CrawlingButton;
