<?php

namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;

class TransferController extends AbstractController
{
    /**
     * @Route("/transfer", name="transfer_list", methods="GET")
     */
    public function index(): Response
    {
        return $this->render('transfer/index.html.twig', [
            'controller_name' => 'TransferController',
        ]);
    }

    /**
     * @Route("/transfer", name="transfer_create", methods="POST")
     */
    public function createAction()
    {

    }
}
