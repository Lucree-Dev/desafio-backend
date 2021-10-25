<?php

namespace App\Controller;

use App\Service\Transfer as ServiceTransfer;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\Routing\Annotation\Route;
use Symfony\Component\Serializer\SerializerInterface;
use Symfony\Component\HttpFoundation\JsonResponse;

class TransferController extends AbstractController
{
    /** SerializerInterface */
    private $serializer;
    /** @var ServiceTransfer */
    private $service;

    public function __construct(
        ServiceTransfer $serviceTransfer,
        SerializerInterface $serializer
        )
    {
        $this->serializer = $serializer;
        $this->service = $serviceTransfer;    
    }

    /**
     * @Route("/bank-statement", name="transfer_list", methods="GET")
     */
    public function index(): Response
    {
        $response = new JsonResponse();
        $response->setContent(
            $this->serializer->serialize(
                $this->service->list(),
                'json'
            )
        );
        return $response;
    }

    /**
     * @Route("/bank-statement/{userId}", name="transfer_list_by_user", methods="GET")
     */
    public function listByUser(int $userId): Response
    {
        $response = new JsonResponse();
        $response->setContent(
            $this->serializer->serialize(
                $this->service->listByUser($userId),
                'json'
            )
        );
        return $response;
    }

    /**
     * @Route("/transfer", name="transfer_create", methods="POST")
     */
    public function createAction(Request $request)
    {
        $transfer = $this->service->create($request->request->all());
        $response = new JsonResponse();
        $response->setContent(
            $this->serializer->serialize(
                $transfer,
                'json'
            )
        );
        return $response;
    }
}
